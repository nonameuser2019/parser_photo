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


def read_input():
    # читает файл с ссылками на категории
    cat_url_list = []
    with open('input.txt', 'r') as r:
        for line in r:
            cat_url_list.append(line.strip('\n'))
    return cat_url_list


url = 'https://traffic-auto.by/datchik-abs/'
html = get_html(url)
soup = BeautifulSoup(html.content, 'html.parser')
card_list = soup.find_all('div', class_='part-item-view')
for card in card_list:
    brand = card.find('div', class_='part-name').find('a').text
    brand_list = brand.split('\n')
    brand_clear = brand_list[1].strip('\t').strip()
    art = brand_list[2].strip('\t').strip()
    link_img = card.find('div', class_='part-photo').find('a').find('img')['data-src']
    logo = link_img.find('logos')
    if logo == -1:
        print(brand_clear, art, link_img)






