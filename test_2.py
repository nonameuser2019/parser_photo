import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

ua = UserAgent()
HEADER = {
    'user-agent': ua.random
}
def get_html(url):
    html = requests.get(url, headers=HEADER)
    if html.status_code == 200:
        return html
    else:
        print(html.status_code)


url = 'https://ukrparts.com.ua/category/tormoznie-diski/c-25/?page=44'
html = get_html(url)
soup = BeautifulSoup(html.content, 'html.parser')
card_list = soup.find_all('div', class_='part_box')
for card in card_list:
    dir_name = card.find('div', class_='part_brand').text
    print(dir_name)




