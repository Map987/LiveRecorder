import os
# 执行pip3安装bilibili-api-python
os.system('pip3 install bilibili-api-python')

from bilibili_api import sync, video_uploader, Credential
from bilibili_api import settings
import bilibili_api
import time
settings.timeout = 100.0
settings.wbi_retry_times = 10 # defaults to 3
settings.request_log = False

async def upload_video(video_path):
    credential = Credential(sessdata=decrypted_sessdata, bili_jct=decrypted_bili_jct, buvid3="")
    vu_meta = video_uploader.VideoMeta(
        tid=130,
        title='title',
        tags=['音乐综合', '音乐'],
        desc='',
        cover="Screenshot_20241128_055608.jpg",
        no_reprint=True
    )
    page = video_uploader.VideoUploaderPage(
        path=video_path,
        title='标题',
        description='简介',
    )
    uploader = video_uploader.VideoUploader([page], vu_meta, credential, line=video_uploader.Lines.WS)
    output = []
    @uploader.on("__ALL__")
    async def ev(data):
        print(data)
        output.append(data)
    await uploader.start()
    return output[-1]
