<img src="https://socialify.git.ci/auqhjjqdo/LiveRecorder/image?font=Inter&forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Auto" alt="LiveRecorder"/>

```
# 下载源码（没有git可以直接从release下载Source code）
!git clone https://github.com/Map987/LiveRecorder
%cd /content/LiveRecorder
# 安装依赖
!python3 -m pip install .
# 源码运行
!python3 live_recorder.py
```

```
Cloning into 'LiveRecorder'...
remote: Enumerating objects: 546, done.
remote: Counting objects: 100% (265/265), done.
remote: Compressing objects: 100% (84/84), done.
remote: Total 546 (delta 225), reused 188 (delta 181), pack-reused 281 (from 1)
Receiving objects: 100% (546/546), 215.42 KiB | 2.48 MiB/s, done.
Resolving deltas: 100% (317/317), done.
/content/LiveRecorder
Processing /content/LiveRecorder
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting streamlink>=6.8.2 (from LiveRecorder==0.1.0)
  Downloading streamlink-7.0.0-py3-none-any.whl.metadata (6.5 kB)
Requirement already satisfied: httpx>=0.27.0 in /usr/local/lib/python3.10/dist-packages (from httpx[http2]>=0.27.0->LiveRecorder==0.1.0) (0.27.2)
Collecting ffmpeg-python>=0.2.0 (from LiveRecorder==0.1.0)
  Downloading ffmpeg_python-0.2.0-py3-none-any.whl.metadata (1.7 kB)
Collecting loguru>=0.7.2 (from LiveRecorder==0.1.0)
  Downloading loguru-0.7.2-py3-none-any.whl.metadata (23 kB)
Collecting jsonpath-ng>=1.6.1 (from LiveRecorder==0.1.0)
  Downloading jsonpath_ng-1.7.0-py3-none-any.whl.metadata (18 kB)
Collecting jsengine>=1.0.7.post1 (from LiveRecorder==0.1.0)
  Downloading jsengine-1.0.7.post1-py2.py3-none-any.whl.metadata (6.0 kB)
Collecting quickjs>=1.19.4 (from LiveRecorder==0.1.0)
  Downloading quickjs-1.19.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl.metadata (590 bytes)
Collecting httpx-socks>=0.9.1 (from httpx-socks[asyncio]>=0.9.1->LiveRecorder==0.1.0)
  Downloading httpx_socks-0.9.2-py3-none-any.whl.metadata (3.0 kB)
Requirement already satisfied: future in /usr/local/lib/python3.10/dist-packages (from ffmpeg-python>=0.2.0->LiveRecorder==0.1.0) (1.0.0)
Requirement already satisfied: anyio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->httpx[http2]>=0.27.0->LiveRecorder==0.1.0) (3.7.1)
Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->httpx[http2]>=0.27.0->LiveRecorder==0.1.0) (2024.8.30)
Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->httpx[http2]>=0.27.0->LiveRecorder==0.1.0) (1.0.7)
Requirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->httpx[http2]>=0.27.0->LiveRecorder==0.1.0) (3.10)
Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.27.0->httpx[http2]>=0.27.0->LiveRecorder==0.1.0) (1.3.1)
Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx>=0.27.0->httpx[http2]>=0.27.0->LiveRecorder==0.1.0) (0.14.0)
Collecting python-socks>=2.0.0 (from httpx-socks>=0.9.1->httpx-socks[asyncio]>=0.9.1->LiveRecorder==0.1.0)
  Downloading python_socks-2.5.3-py3-none-any.whl.metadata (7.0 kB)
Requirement already satisfied: async-timeout>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from httpx-socks[asyncio]>=0.9.1->LiveRecorder==0.1.0) (4.0.3)
Collecting h2<5,>=3 (from httpx[http2]>=0.27.0->LiveRecorder==0.1.0)
  Downloading h2-4.1.0-py3-none-any.whl.metadata (3.6 kB)
Collecting ply (from jsonpath-ng>=1.6.1->LiveRecorder==0.1.0)
  Downloading ply-3.11-py2.py3-none-any.whl.metadata (844 bytes)
Collecting isodate (from streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading isodate-0.7.2-py3-none-any.whl.metadata (11 kB)
Requirement already satisfied: lxml<6,>=4.6.4 in /usr/local/lib/python3.10/dist-packages (from streamlink>=6.8.2->LiveRecorder==0.1.0) (5.3.0)
Collecting pycountry (from streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading pycountry-24.6.1-py3-none-any.whl.metadata (12 kB)
Collecting pycryptodome<4,>=3.4.3 (from streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.10/dist-packages (from streamlink>=6.8.2->LiveRecorder==0.1.0) (1.7.1)
Requirement already satisfied: requests<3,>=2.26.0 in /usr/local/lib/python3.10/dist-packages (from streamlink>=6.8.2->LiveRecorder==0.1.0) (2.32.3)
Collecting trio-websocket<1,>=0.9.0 (from streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading trio_websocket-0.11.1-py3-none-any.whl.metadata (4.7 kB)
Requirement already satisfied: typing-extensions>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlink>=6.8.2->LiveRecorder==0.1.0) (4.12.2)
Requirement already satisfied: urllib3<3,>=1.26.0 in /usr/local/lib/python3.10/dist-packages (from streamlink>=6.8.2->LiveRecorder==0.1.0) (2.2.3)
Requirement already satisfied: websocket-client<2,>=1.2.1 in /usr/local/lib/python3.10/dist-packages (from streamlink>=6.8.2->LiveRecorder==0.1.0) (1.8.0)
Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from streamlink>=6.8.2->LiveRecorder==0.1.0) (1.2.2)
Collecting trio<1,>=0.22.0 (from streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading trio-0.27.0-py3-none-any.whl.metadata (8.6 kB)
Collecting hyperframe<7,>=6.0 (from h2<5,>=3->httpx[http2]>=0.27.0->LiveRecorder==0.1.0)
  Downloading hyperframe-6.0.1-py3-none-any.whl.metadata (2.7 kB)
Collecting hpack<5,>=4.0 (from h2<5,>=3->httpx[http2]>=0.27.0->LiveRecorder==0.1.0)
  Downloading hpack-4.0.0-py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.26.0->streamlink>=6.8.2->LiveRecorder==0.1.0) (3.4.0)
Requirement already satisfied: attrs>=23.2.0 in /usr/local/lib/python3.10/dist-packages (from trio<1,>=0.22.0->streamlink>=6.8.2->LiveRecorder==0.1.0) (24.2.0)
Collecting sortedcontainers (from trio<1,>=0.22.0->streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl.metadata (10 kB)
Collecting outcome (from trio<1,>=0.22.0->streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading outcome-1.3.0.post0-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting wsproto>=0.14 (from trio-websocket<1,>=0.9.0->streamlink>=6.8.2->LiveRecorder==0.1.0)
  Downloading wsproto-1.2.0-py3-none-any.whl.metadata (5.6 kB)
Downloading ffmpeg_python-0.2.0-py3-none-any.whl (25 kB)
Downloading httpx_socks-0.9.2-py3-none-any.whl (12 kB)
Downloading jsengine-1.0.7.post1-py2.py3-none-any.whl (17 kB)
Downloading jsonpath_ng-1.7.0-py3-none-any.whl (30 kB)
Downloading loguru-0.7.2-py3-none-any.whl (62 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.5/62.5 kB 4.7 MB/s eta 0:00:00
Downloading quickjs-1.19.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl (2.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 31.8 MB/s eta 0:00:00
Downloading streamlink-7.0.0-py3-none-any.whl (531 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 531.2/531.2 kB 24.9 MB/s eta 0:00:00
Downloading h2-4.1.0-py3-none-any.whl (57 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.5/57.5 kB 4.5 MB/s eta 0:00:00
Downloading pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 34.9 MB/s eta 0:00:00
Downloading python_socks-2.5.3-py3-none-any.whl (52 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 52.9/52.9 kB 3.7 MB/s eta 0:00:00
Downloading trio-0.27.0-py3-none-any.whl (481 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 481.7/481.7 kB 22.6 MB/s eta 0:00:00
Downloading trio_websocket-0.11.1-py3-none-any.whl (17 kB)
Downloading isodate-0.7.2-py3-none-any.whl (22 kB)
Downloading ply-3.11-py2.py3-none-any.whl (49 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.6/49.6 kB 3.6 MB/s eta 0:00:00
Downloading pycountry-24.6.1-py3-none-any.whl (6.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 41.7 MB/s eta 0:00:00
Downloading hpack-4.0.0-py3-none-any.whl (32 kB)
Downloading hyperframe-6.0.1-py3-none-any.whl (12 kB)
Downloading wsproto-1.2.0-py3-none-any.whl (24 kB)
Downloading outcome-1.3.0.post0-py2.py3-none-any.whl (10 kB)
Downloading sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)
Building wheels for collected packages: LiveRecorder
  Building wheel for LiveRecorder (pyproject.toml) ... done
  Created wheel for LiveRecorder: filename=LiveRecorder-0.1.0-py3-none-any.whl size=9465 sha256=aec57e28116753866d0cab20d688557a0dd1f9b09b02d82855906badd3bbb6d2
  Stored in directory: /tmp/pip-ephem-wheel-cache-gk_vu63_/wheels/5d/d3/8c/cd9d6d39fe560993dba3fca578c40852ff3b13f293b9c39992
Successfully built LiveRecorder
Installing collected packages: sortedcontainers, quickjs, python-socks, ply, wsproto, pycryptodome, pycountry, outcome, loguru, jsonpath-ng, jsengine, isodate, hyperframe, hpack, ffmpeg-python, trio, h2, trio-websocket, httpx-socks, streamlink, LiveRecorder
Successfully installed LiveRecorder-0.1.0 ffmpeg-python-0.2.0 h2-4.1.0 hpack-4.0.0 httpx-socks-0.9.2 hyperframe-6.0.1 isodate-0.7.2 jsengine-1.0.7.post1 jsonpath-ng-1.7.0 loguru-0.7.2 outcome-1.3.0.post0 ply-3.11 pycountry-24.6.1 pycryptodome-3.21.0 python-socks-2.5.3 quickjs-1.19.4 sortedcontainers-2.4.0 streamlink-7.0.0 trio-0.27.0 trio-websocket-0.11.1 wsproto-1.2.0
2024-11-26 21:01:57.382 | INFO     | __main__:start:53 - [Bilibili][方便]正在检测直播状态
2024-11-26 21:01:57.383 | INFO     | __main__:start:54 - 预配置刷新间隔：10s
1
2024-11-26 21:01:58.057 | INFO     | __main__:get_streamlink:140 - 是否验证SSL：True
2024-11-26 21:01:58.993 | INFO     | __main__:run_record:158 - [Bilibili][方便]开始录制：[2024.11.26 21.01.58][Bilibili][方便]LofiGirl的音乐自习室.flv
2024-11-26 21:01:58.995 | INFO     | __main__:stream_writer:170 - [Bilibili][方便]获取到直播流链接：[2024.11.26 21.01.58][Bilibili][方便]LofiGirl的音乐自习室.flv
https://d1--ov-gotcha207.bilivideo.com/live-bvc/763559/live_1685650605_47688319_2500/index.m3u8?expires=1732658518&len=0&oi=581816395&pt=web&qn=250&trid=1007ccc22aa2a56f3d85267f5c1aae4390c5&sigparams=cdn,expires,len,oi,pt,qn,trid&cdn=ov-gotcha207&sign=4187c71d80b2426da24ea2a9521e275a&site=25d5ee71f84869eddf72782415ccdbd7&free_type=0&mid=0&sche=ban&bvchls=1&trace=0&isp=other&rg=other&pv=other&deploy_env=prod&sl=1&sk=5bf07b9bbe6df2e0a6bc476fe3d9a64272675319e1bf242748fcda5ad9e12f7b&source=puv3_onetier&pp=rtmp&score=30&hot_cdn=0&origin_bitrate=658158&suffix=2500&p2p_type=-1&flvsk=4207df3de646838b084f14f252be3aff32e9f79d88eba2913a6cbca8199656ed&vd=bc&src=puv3&order=1
2024-11-26 21:02:00.485 | INFO     | __main__:stream_writer:176 - [Bilibili][方便]正在录制：[2024.11.26 21.01.58][Bilibili][方便]LofiGirl的音乐自习室.flv
[download] Written 157.52 MiB to …58][Bilibili][方便]LofiGirl的音乐自习室.flv (27m42s @ 92.18 KiB/s)2024-11-26 21:29:42.627 | WARNING  | __main__:run:236 - 用户中断录制，正在关闭直播流
[download] Written 157.52 MiB to …58][Bilibili][方便]LofiGirl的音乐自习室.flv (27m42s @ 93.05 KiB/s)
2024-11-26 21:29:42.954 | INFO     | __main__:run_ffmpeg:193 - [Bilibili][方便]开始ffmpeg封装：[2024.11.26 21.01.58][Bilibili][方便]LofiGirl的音乐自习室.flv
[h264 @ 0x56a211e89100] co located POCs unavailable
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'bilibili_鹿乃/[2024.11.26 21.01.58][Bilibili][方便]LofiGirl的音乐自习室.flv':
  Metadata:
    major_brand     : isom
    minor_version   : 1
    compatible_brands: isommp42avc1dash
  Duration: 07:24:50.41, start: 25026.284000, bitrate: 49 kb/s
  Stream #0:0(und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1280x720, 38 kb/s, 30 fps, 30 tbr, 90k tbn, 60 tbc (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
      encoder         : (libobs version 30.2.3),BILIAV
  Stream #0:1(und): Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 10 kb/s (default)
    Metadata:
      handler_name    : SoundHandler
      vendor_id       : [0][0][0][0]
Output #0, mp4, to 'bilibili_鹿乃/[2024.11.26 21.01.58][Bilibili][方便]LofiGirl的音乐自习室.mp4':
  Metadata:
    encoder         : Lavf58.76.100
  Stream #0:0: Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1280x720, q=2-31, 38 kb/s, 30 fps, 30 tbr, 90k tbn, 90k tbc (default)
  Stream #0:1: Audio: aac (LC) (mp4a / 0x6134706D), 48000 Hz, stereo, fltp, 10 kb/s (default)
Stream mapping:
  Stream #0:0 -> #0:0 (copy)
  Stream #0:1 -> #0:1 (copy)
Press [q] to stop, [?] for help
[mp4 @ 0x56a211f87400] Starting second pass: moving the moov atom to the beginning of the file
frame=49860 fps=41710 q=-1.0 Lsize=  161324kB time=00:27:44.10 bitrate= 794.2kbits/s speed=1.39e+03x    
video:126201kB audio:32958kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 1.360808%

```

## 简介

一款无人值守直播录制脚本，基于强大的[Streamlink](https://streamlink.github.io)
实现多平台直播源录制，通过挖掘直播平台官方API以轮询方式实现直播开播检测，致力于用最少的代码实现最多的功能

## 已支持平台

- [x] 哔哩哔哩
- [x] 斗鱼
- [x] 虎牙
- [x] 抖音
- [x] YouTube
- [x] Twitch
- [x] NicoNico
- [x] TwitCasting
- [x] Afreeca
- [x] Pandalive
- [x] Bigolive
- [x] Pixiv Sketch
- [x] Chaturbate
- [ ] 更多平台欢迎PR

## 说明

- 不建议同时录制过多直播，可能会出现不可预见的问题
- 部分直播平台（如Pandalive）存在风控，请谨慎使用
- 因个人精力有限，小众直播平台的支持可能存在问题，新增直播平台欢迎PR
- 本脚本仅用于无人值守录制，有关UI界面和录制拆分等通过后期软件可以实现的功能不考虑添加

## 已知bug

- YouTube在录制单个频道多开直播间时会出现频繁中断，暂时无法修复
- 斗鱼直播因使用js引擎可能出现偶发的解析错误，会自动重试录制
- Bigolive存在部分用户录制花屏，原因未知

## 使用

### 安装FFmpeg

[FFmpeg官方下载页面](https://ffmpeg.org/download.html)

根据你的运行平台安装对应版本，并添加环境变量确保全局调用

### 下载

当前支持Windows, Mac和Linux平台（amd64架构），请前往Release下载对应平台的可执行程序

[Release下载页面](https://github.com/auqhjjqdo/LiveRecorder/releases)

下载解压后修改配置，直接运行二进制文件即可

### 源码运行

在不支持的平台运行时可使用源码运行，安装好Python后在命令行输入以下命令即可

```shell
# 下载源码（没有git可以直接从release下载Source code）
git clone https://github.com/auqhjjqdo/LiveRecorder.git
cd LiveRecorder
# 安装依赖
python3 -m pip install .
# 源码运行
python3 live_recorder.py
```

## 配置

配置文件存储于`config.json`，该文件位于可执行程序相同目录

修改示例配置文件`config.sample.json`后务必重命名为`config.json`

文件内容要求严格按照json语法，请前往[在线json格式化网站](https://www.bejson.com/)校验后再修改

### 代理配置

`proxy`的值为代理地址，支持http和socks代理，格式为`protocol://[user:password@]ip:port`

例如`http://127.0.0.1:7890`、`socks5://admin:passwd@127.0.0.1:1080`

建议优先使用http代理，目前socks5代理存在一定兼容性问题

无需代理时去除引号填写`null`或删除该字段即可

### 输出目录配置

`output`字段为录制文件输出后保存的目录路径，非必填字段（请勿填写空字符串），默认输出到运行目录的`output`文件夹

路径分隔符请使用`/`，防止出现转义导致的不兼容问题

支持相对路径和绝对路径，例如`output/video`、`/tmp/output`、`D:/output`

### 直播录制配置

按照示例修改`user`列表，注意逗号、引号和缩进

| 字段       | 含义          | 可填内容                                                                                        | 是否必填 | 备注                             |
|----------|-------------|---------------------------------------------------------------------------------------------|------|--------------------------------|
| platform | 直播平台        | 直播平台的英文名或拼音                                                                                 | 必填   | 必须为首字母大写                       |
| id       | 直播用户id      | 直播平台的房间号或用户名                                                                                | 必填   | 参考config文件示例格式<br/>一般在直播网址即可找到 |
| name     | 自定义主播名      | 任意字符                                                                                        | 非必填  | 用于录制文件区分<br/>未填写时默认使用id        |
| interval | 检测间隔        | 任意整数或小数                                                                                     | 非必填  | 默认检测间隔为10秒                     |
| format   | 输出格式        | 例如`ts`、`flv`、`mp4`、`mkv`等<br/>详见[FFmpeg官方文档](https://ffmpeg.org/ffmpeg-formats.html#Muxers) | 非必填  | 默认使用直播平台的直播流输出格式               |
| output   | 输出目录        | 与[输出目录配置](#输出目录配置)相同                                                                        | 非必填  | 优先级高于[输出目录配置](#输出目录配置)         |
| proxy    | 代理          | 与[代理配置](#代理配置)相同                                                                            | 非必填  | 优先级高于[代理配置](#代理配置)             |
| headers  | HTTP 标头     | 参考[官方文档](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers)                         | 非必填  | 可用于部分需请求头验证的网站                 |
| cookies  | HTTP Cookie | `key=value`<br/>多个cookie使用`;`分隔                                                             | 非必填  | 可用于录制需登录观看的直播                  |

### 注意事项

#### 哔哩哔哩的房间号

部分主播的B站房间号在使用网页打开时地址栏默认显示的是短号，并不是真实的房间号，如需获取真实房间号可以打开

`https://api.live.bilibili.com/xlive/web-room/v2/index/getRoomPlayInfo?room_id=短号`

返回的数据中`room_id`后的数字即真实房间号

#### 哔哩哔哩的清晰度

由于哔哩哔哩的限制，未登录用户无法观看较高画质的直播，因此需要在配置文件中添加`cookies`字段（仅需`SESSDATA`）以获取原画清晰度的直播流

#### 斗鱼的房间号

斗鱼直播同哔哩哔哩在部分直播间的房间号显示的是短号，获取真实房间号可打开F12开发者工具，在控制台输入`room_id`，返回的数字即真实房间号

#### YouTube的频道ID

YouTube的频道ID一般是由`UC`开头的一段字符，由于YouTube可以自定义标识名，打开YouTube频道时网址会优先显示标识名而非频道ID

获取YouTube的频道ID可以使用以下网站：

https://seostudio.tools/zh/youtube-channel-id

https://ytgear.com/youtube-channel-id


#### NicoNico的用户ID和频道ID

NicoNico的直播分为用户直播和频道直播，其ID分别以`co`和`ch`开头再加上一段数字，但NicoNico的直播间一般是以`lv`开头的视频ID，获取用户ID或频道ID可在F12开发者工具的控制台输入`NicoGoogleTagManagerDataLayer[0].content`，在返回的数据中`community_id`或`channel_id`的值即对应的用户ID或频道ID

其中部分频道在使用频道ID时无法获取到最新直播，此问题暂时无解，请使用`lv`视频ID代替

#### TwitCasting的检测间隔

由于直播检测请求使用了HTTP
Keep-Alive长连接防止频繁建立TCP通道导致性能下降，但TwitCasting的服务器要求10秒内无请求则关闭连接，所以配置文件在添加TwitCasting的直播时尽量加入`interval`
字段并将检测间隔设为小于10秒，以免频繁出现请求协议错误

## 输出文件

输出文件会在录制结束后使用ffmpeg封装为配置文件自定义的输出格式，音视频编码为直播平台直播流默认（一般视频编码为`H.264`
，音频编码为`AAC`），录制清晰度为最高画质，封装结束后自动删除原始录制文件，输出格式为空或未填写时不进行封装

输出文件名命名格式为`[年.月.日 时.分.秒][平台][主播名]直播标题.格式`，日期时区为系统默认时区
