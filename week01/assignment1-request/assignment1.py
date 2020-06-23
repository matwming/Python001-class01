import requests
from bs4 import BeautifulSoup
from typing import Dict

request_settings = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Accept': "*/*",
    'Accept-Encoding': 'gazip, deflate, br',
    'Accept-Language': 'en-AU,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
    'Content-Type': 'text/plain',
    'Connection': 'keep-alive',
    'Host': 'wreport1.meituan.net',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/films?showType=3',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

cookie: Dict[str, str] = {
    '_lxsdk_s': '172e160d2f5-d3c-12-056%7C%7C9',
    '_lxsdk': 'E6EA16D0B55511EA9C0AF732B1940F47333B3F49B24A44A69D71339E9660483C',
    '__mta': '220691367.1592919119180.1592919735384.1592920807858.5',
    '_lxsdk_cuid': '172e160d2f4c8-03eb7b64f6bd08-31607402-1fa400-172e160d2f4c8',
    'mojo-session-id': '{"id":"c68533077a8cc469069a43b2de1659c3","time":1592919118390}',
    '_csrf': '17d7eb37864ea439b13c723541828c51462f67904c66165fb476235d25966905',
    'mojo-trace-id': '5',
    'uuid': 'E6EA16D0B55511EA9C0AF732B1940F47333B3F49B24A44A69D71339E9660483C',
    'mojo-uuid': 'cccd4ad4647d90e2b94b84db623ced15',
    'uuid_n_v': 'v1'
}
url: str = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=request_settings, cookies=cookie)

print(response.text)
print(f'返回码是: {response.status_code}')
