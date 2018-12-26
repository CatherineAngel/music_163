#parse_song_id(songer_id)
#这个函数功能：输出参数歌手id，输出歌曲id
#这个只有热门单曲50，具体其他得自行查找


import requests
from lxml import etree
def parse_song_id(songer_id):
        headers={
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=56f13d1f1f486e6766b92885b11f92ef,1545551450754; _ntes_nuid=56f13d1f1f486e6766b92885b11f92ef; WM_TID=2x6nxVuLYbJFUAAAAAdpe%2BPIAYqX%2BsXx; __utmc=94650624; __utmz=94650624.1545735057.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=5lxQ6%2FWpLI8I%2B2VsYggHDUAlHym1aVzcXTsbJSHBcgQWtdT6qLAMN%2F4n5ilL7reukxmAEAKzDkZfyhKoOBK6nswZKxzDp4bFWH%2FqPfA%2FpbiODvj0lruZKGufNTb5HaxUVE4%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee98e460b0b99c87f733f7928ab2d55b869f9aabf36ab3a9a893f5538d949cb8c22af0fea7c3b92af7b4b8b2b52595b084aabb43e9ee9a94dc6da5988cb6c4688ca7a3d2e45ebabd98b5f26a8a8d88a3e26d9389bc85d73eb3948faecd25f8b2fb8aef48f5aeab96ea74af9f8ba2ca7288b59687fc6489b181a3ca3eaeadb9bbca74ba9cc0d5e14e9598e192d36e83f1c083ec4588aaa6d1ef7ab78685a8f86e8e8caed6cb6bbc8b9aa6b737e2a3; __utma=94650624.1042807263.1545551453.1545735057.1545741311.6; JSESSIONID-WYYY=wbd5Yp40jYOCX%2B7b%5CiaAlef%2F3Syih%5CUbshMqjQWCR9ZbOHznlOi2Igsvg%2FwUKmdKUiqgnZ50VslyVXw4Zd3R6YUMH1nxy%2B%2BW9CriJ4OrNEIRMNxemg5HxaQXwoFg4QZ%2FYpGSiuxtcZ7Or%5CICU%5C1fug6GUG6N2dkTeA8Rz2%2Fdkno%2F%2BtXY%3A1545744153276; __utmb=94650624.15.10.1545741311',
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        url='https://music.163.com/artist?id='+str(songer_id)
        res=requests.get(url,headers=headers)
        # print(res.text)
        html=etree.HTML(res.text)
        song_url=html.xpath("//ul[@class='f-hide']/li/a/@href")
        song_name = html.xpath("//ul[@class='f-hide']/li/a/text()")
        info={}
        for url,name in zip(song_url,song_name):
                info[url[9:]]=name
        return info
        # return song_id

# parse_song_id(5781)
