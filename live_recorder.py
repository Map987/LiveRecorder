import asyncio
import json
import os
import re
import time
import uuid
from http.cookies import SimpleCookie
from pathlib import Path
from typing import Dict, Tuple, Union
from urllib.parse import parse_qs

import anyio
import ffmpeg
import httpx
import jsengine
import streamlink
from httpx_socks import AsyncProxyTransport
from jsonpath_ng.ext import parse
from loguru import logger
from streamlink.options import Options
from streamlink.stream import StreamIO, HTTPStream, HLSStream
from streamlink_cli.main import open_stream
from streamlink_cli.output import FileOutput
from streamlink_cli.streamrunner import StreamRunner

recording: Dict[str, Tuple[StreamIO, FileOutput]] = {}


class LiveRecoder:
    def __init__(self, config: dict, user: dict):
        self.id = user['id']
        platform = user['platform']
        name = user.get('name', self.id)
        self.flag = f'[{platform}][{name}]'
        
        self.interval = user.get('interval', 10)
        self.crypto_js_url = user.get('crypto_js_url', '')
        self.headers = user.get('headers', {'User-Agent': 'Chrome'})
        self.cookies = user.get('cookies')
        self.format = user.get('format')
        self.proxy = user.get('proxy', config.get('proxy'))
        self.output = user.get('output', config.get('output', 'output'))
        if not self.crypto_js_url:
            self.crypto_js_url = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js'
        self.get_cookies()
        self.client = self.get_client()

    async def start(self):
        self.ssl = True
        self.mState = 0
        while True:
            try:
                logger.info(f'{self.flag}正在检测直播状态')
                logger.info(f'预配置刷新间隔：{self.interval}s')
                try:
                    await self.run()   
                except Exception as run_error:
                    logger.error(f"{self.flag}直播检测内部错误\n{repr(run_error)}")
                state = self.mState
                timeI = self.interval
                if state == '1':
                    timeI = 2
                logger.info(f'->直播状态：{state}  实际刷新间隔：{timeI}s')
                await asyncio.sleep(timeI)
            except ConnectionError as error:
                if '直播检测请求协议错误' not in str(error):
                    logger.error(error)
                await self.client.aclose()
                self.client = self.get_client()
            except Exception as error:
                logger.exception(f'{self.flag}直播检测错误\n{repr(error)}')

    async def run(self):
        pass

    async def request(self, method, url, **kwargs):
        try:
            response = await self.client.request(method, url, **kwargs)
            return response
        except httpx.ProtocolError as error:
            raise ConnectionError(f'{self.flag}直播检测请求协议错误\n{error}')
        except httpx.HTTPStatusError as error:
            raise ConnectionError(
                f'{self.flag}直播检测请求状态码错误\n{error}\n{response.text}')
        except anyio.EndOfStream as error:
            raise ConnectionError(f'{self.flag}直播检测代理错误\n{error}')
        except httpx.HTTPError as error:
           logger.error(f'网络异常 重试...')
           raise ConnectionError(f'{self.flag}直播检测请求错误\n{repr(error)}')
		
           

    def get_client(self):
        client_kwargs = {
            'http2': True,
            'timeout': self.interval,
            'limits': httpx.Limits(max_keepalive_connections=100, keepalive_expiry=self.interval * 2),
            'headers': self.headers,
            'cookies': self.cookies
        }
        # 检查是否有设置代理
        if self.proxy:
            if 'socks' in self.proxy:
                client_kwargs['transport'] = AsyncProxyTransport.from_url(self.proxy)
            else:
                client_kwargs['proxies'] = self.proxy
        return httpx.AsyncClient(**client_kwargs)

    def get_cookies(self):
        if self.cookies:
            cookies = SimpleCookie()
            cookies.load(self.cookies)
            self.cookies = {k: v.value for k, v in cookies.items()}

    def get_filename(self, title, format):
        live_time = time.strftime('%Y.%m.%d %H.%M.%S')
        # 文件名特殊字符转换为全角字符
        char_dict = {
            '"': '＂',
            '*': '＊',
            ':': '：',
            '<': '＜',
            '>': '＞',
            '?': '？',
            '/': '／',
            '\\': '＼',
            '|': '｜'
        }
        for half, full in char_dict.items():
            title = title.replace(half, full)
        filename = f'[{live_time}]{self.flag}{title[:50]}.{format}'
        return filename

    def get_streamlink(self):
        session = streamlink.session.Streamlink({
            'stream-segment-timeout': 60,
            'hls-segment-queue-threshold': 10
        })
        ssl = self.ssl
        logger.info(f'是否验证SSL：{ssl}')
        session.set_option('http-ssl-verify', ssl)
        # 添加streamlink的http相关选项
        if proxy := self.proxy:
            # 代理为socks5时，streamlink的代理参数需要改为socks5h，防止部分直播源获取失败
            if 'socks' in proxy:
                proxy = proxy.replace('://', 'h://')
            session.set_option('http-proxy', proxy)
        if self.headers:
            session.set_option('http-headers', self.headers)
        if self.cookies:
            session.set_option('http-cookies', self.cookies)
        return session

    def run_record(self, stream: Union[StreamIO, HTTPStream], url, title, format):
        # 获取输出文件名
        filename = self.get_filename(title, format)
        if stream:
            logger.info(f'{self.flag}开始录制：{filename}')
            # 调用streamlink录制直播
            result = self.stream_writer(stream, url, filename)
            # 录制成功、format配置存在且不等于直播平台默认格式时运行ffmpeg封装
            if result and self.format and self.format != format:
                self.run_ffmpeg(filename, format)
            recording.pop(url, None)
            logger.info(f'{self.flag}停止录制：{filename}')
        else:
            logger.error(f'{self.flag}无可用直播源：{filename}')

    def stream_writer(self, stream, url, filename):
        logger.info(f'{self.flag}获取到直播流链接：{filename}\n{stream.url}')
        output = FileOutput(Path(f'{self.output}/{filename}'))
        try:
            stream_fd, prebuffer = open_stream(stream)
            output.open()
            recording[url] = (stream_fd, output)
            logger.info(f'{self.flag}正在录制：{filename}')
            StreamRunner(stream_fd, output, show_progress=True).run(prebuffer)
            return True
        except Exception as error:
            if 'timeout' in str(error):
                logger.warning(f'{self.flag}直播录制超时，请检查主播是否正常开播或网络连接是否正常：{filename}\n{error}')
            elif re.search(f'SSL: CERTIFICATE_VERIFY_FAILED', str(error)):
                logger.warning(f'{self.flag}SSL错误，将取消SSL验证：{filename}\n{error}')
                self.ssl = False
            elif re.search(f'(Unable to open URL|No data returned from stream)', str(error)):
                logger.warning(f'{self.flag}直播流打开错误，请检查主播是否正常开播：{filename}\n{error}')
            else:
                logger.exception(f'{self.flag}直播录制错误：{filename}\n{error}')
        finally:
            output.close()

    def run_ffmpeg(self, filename, format):
        logger.info(f'{self.flag}开始ffmpeg封装：{filename}')
        new_filename = filename.replace(f'.{format}', f'.{self.format}')
        ffmpeg.input(f'{self.output}/{filename}').output(
            f'{self.output}/{new_filename}',
            codec='copy',
            map_metadata='-1',
            movflags='faststart'
        ).global_args('-hide_banner').run()
        os.remove(f'{self.output}/{filename}')


class Bilibili(LiveRecoder):
    async def run(self):
        url = f'https://live.bilibili.com/{self.id}'
        if url not in recording:
	    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
                'Referer': 'https://www.bilibili.com'  # 添加 Referer 字段
		    
            response = (await self.request(
                method='GET',
                url='https://api.live.bilibili.com/room/v1/Room/get_info',
                params={'room_id': self.id},
		headers=headers
            )).json()
            if response['data']['live_status']
              print(response['data']['live_status'])
            if response['data']['live_status'] == 1:
                title = response['data']['title']
                stream = self.get_streamlink().streams(url).get('best')  # HTTPStream[flv]
                await asyncio.to_thread(self.run_record, stream, url, title, 'flv')

async def run():
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    try:
        tasks = []
        for item in config['user']:
            platform_class = globals()[item['platform']]
            coro = platform_class(config, item).start()
            tasks.append(asyncio.create_task(coro))
        await asyncio.wait(tasks)
    except (asyncio.CancelledError, KeyboardInterrupt, SystemExit):
        logger.warning('用户中断录制，正在关闭直播流')
        for stream_fd, output in recording.copy().values():
            stream_fd.close()
            output.close()


if __name__ == '__main__':
    logger.add(
        sink='logs/log_{time:YYYY-MM-DD}.log',
        rotation='00:00',
        retention='3 days',
        level='INFO',
        encoding='utf-8',
        format='[{time:YYYY-MM-DD HH:mm:ss}][{level}][{name}][{function}:{line}]{message}'
    )
    asyncio.run(run())
