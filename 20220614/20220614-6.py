import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()


if __name__ == '__main__':
    main()
#重點：異步I/O與多進程的比較。
#當程序不需要真正的並發性或併行性，而是更多的依賴於異步處理和回調時，asyncio就是一種很好的選擇。
#如果程序中有大量的等待與休眠時，也應該考慮asyncio，它很適合編寫沒有實時數據處理需求的Web應用服務器。