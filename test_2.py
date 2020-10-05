import requests
from fake_useragent import UserAgent


ua = UserAgent()
HEADER = {
    'user-agent': ua.random
}
url = 'https://altstar.com.ua/starter?mfp=77-oem-original-nyy-proizvoditel%5BBOSCH%5D%3Fpage%3D152&page=1'
response = requests.get(url, headers=HEADER)
print(response.status_code)


