import requests
import base64
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

import urllib.request
import urllib.parse
import re
from cryptography.fernet import Fernet
import json
# URL of the text
url = "https://api.github.com/repos/Map987/BAAS/contents/cookie.env"

# Bearer Token
import sys
bearer_token = sys.argv[1]
encode_code = sys.argv[2]
#bearer_token = "………"
#encode_code = "………"
# Create a request object with the Bearer Token
req = urllib.request.Request(url)
req.add_header("Authorization", f"Bearer {bearer_token}")
req.add_header("Accept", "application/vnd.github.v3.raw")

# Fetching the text from the URL
response = urllib.request.urlopen(req)
txt = response.read().decode('utf-8')
print(txt)
# Extracting the values using regex
sessdata_match = re.search(r"SESSDATA=b'(.*?)'", txt)
bili_jct_match = re.search(r"BIILI_JCT=b'(.*?)'", txt)
refresh_token_match = re.search(r"REFRESH_TOKEN=b'(.*?)'", txt)

# Extracted values
sessdata_value = sessdata_match.group(1) if sessdata_match else None
bili_jct_value = bili_jct_match.group(1) if bili_jct_match else None
refresh_token_value = refresh_token_match.group(1) if refresh_token_match else None

key_bytes = (encode_code.encode())
fernet = Fernet(key_bytes)

try:
    decrypted_sessdata = fernet.decrypt(sessdata_value).decode()
    decrypted_bili_jct = fernet.decrypt(bili_jct_value).decode()
    decrypted_refresh_token = fernet.decrypt(refresh_token_value).decode()
except Exception as e:
    decrypted_sessdata, decrypted_bili_jct, decrypted_refresh_token, error = None, None, None, str(e)

decrypted_sessdata, decrypted_bili_jct, decrypted_refresh_token, error if 'error' in locals() else ''


import os

def get_video_paths(folder_path):
    video_extensions = ['.mp4', '.flv', '.mov', '.mkv', '.flv', '.wmv', '.mpg', '.mpeg', '.m4v', '.3gp', '.3g2', '.webm', '.ts']
    video_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in video_extensions):
                video_paths.append(os.path.join(root, file))

    return video_paths

folder_checkpoint = "checkpoint"
os.makedirs(folder_checkpoint, exist_ok=True)

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
        self.event = asyncio.Event()
    def check_checkpoint(self):
        check_path = os.path.join(folder_checkpoint, f"{self.id}.txt")
        if not os.path.exists(check_path): #txt文件，录制时候内容为1，结束录制修改为0
            with open(check_path, 'w') as f:
                f.write('0')
        
        try:
            with open(check_path, 'r') as f:
                content = f.read().strip()
            return content == '1'
        except IOError:
            logger.error('无法读取checkpoint.txt文件')
            return False



    def update_checkpoint(self, value):
        FILE = f"checkpoint/{self.id}.txt"  # 文件路径
        headers = {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': f'token {bearer_token}'
        }

        response = requests.get(
            f'https://api.github.com/repos/{self.REPO}/contents/{FILE}',
            headers=headers,
        )
        sha = response.json().get("sha")

        # 假设content变量已经被定义，并且是一个字符串
        content = str(value)

        # 将内容转换为base64编码
        encoded_content = base64.b64encode(content.encode()).decode()

        data = {
            "message": "测试测试这里的是上传commit描述",
            "content": encoded_content,
            "sha": sha
        }

        put_response = requests.put(
            f'https://api.github.com/repos/{self.REPO}/contents/{FILE}',
            headers=headers,
            json=data
        )

    async def start(self):
        self.ssl = True
        self.mState = 0
        while not self.event.is_set():
#while True:
            if self.check_checkpoint():
                break#每5分运行一次，如果正在直播，把一个room_id.txt文件内容修改为1，别的GitHub action检测到room_id.txt为1，则break该action内该房间的录制

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
        #filename = f'[{live_time}]{self.flag}{title[:50]}.{format}'
        filename = f'[{live_time}]{title[:50]}.{format}' 
	    #文件夹 bilibili_鹿乃 ，文件名 [2024.11.26 21.01.58][Bilibili][方便]LofiGirl的音乐自习室.mp4'
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
            self.update_checkpoint(1) #开始录制，更新checkpoint/{self.room_id}txt文件内容为1，别的GitHub action任务，检测到为1就break执行，确保只有一个任务代码在录制
            result = self.stream_writer(stream, url, filename)
            # 录制成功、format配置存在、且不等于直播平台默认格式时，运行ffmpeg封装

            #暂停怎么也能到这里
            if result:#每5分运行一次，如果正在直播，把一个room_id.txt文件内容修改为1，别的GitHub action检测到room_id.txt为1则break该直播，此处是直播完重新修改为0
                self.update_checkpoint(0)
		    
            if result and self.format and self.format != format:
                self.run_ffmpeg(filename, format)
            recording.pop(url, None)
            video_paths = get_video_paths(self.output)
            for video_path in video_paths:
                    import upload
                    from upload import upload_video #如果没有 import upload，可能只有upload.py里面的def upload_video函数，没有里面的其他包import
                    result = upload_video(video_path)
                    print(result)
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
	    }
            response = (await self.request(
                method='GET',
                url='https://api.live.bilibili.com/room/v1/Room/get_info',
                params={'room_id': self.id},
		headers=headers
            )).json()
            if response['data']['live_status']:
                print(response['data']['live_status'])
            if response['data']['live_status'] != 1:
                self.event.set()
                return #不需要循环检查
            if response['data']['live_status'] == 1:

                with open(f"{self.id}.txt", "w") as f:
                    f.write("1")
                title = response['data']['title']
                stream = self.get_streamlink().streams(url).get('best')  # HTTPStream[flv]
		#这行代码首先调用  self.get_streamlink()  方法来创建一个  streamlink会话，self.get_streamlink返回session，也就是session=streamlink.session.Streamlink， 然后使用  session.streams(url)  方法来获取给定 URL 的所有可用流。streams(url)本质就是把url，也就是live.bilibili.com去正则等等匹配b站插件https://github.com/streamlink/streamlink/blob/master/src/streamlink/plugins/bilibili.py  文档 https://streamlink.github.io/api/session.html
                #from streamlink.stream import StreamIO, HTTPStream, HLSStream
		     #streamlink.stream传入https://api.live.bilibili.com/room/v1/Room/get_info链接，去查询streamlink的b站下载功能
                print(f"房间{self.id} streams(url)方法", self.get_streamlink().streams(url))
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
