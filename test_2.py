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


url = 'https://ukrparts.com.ua/category/tormoznie-diski/c-25/'
url_list = read_input()
print(url_list)




