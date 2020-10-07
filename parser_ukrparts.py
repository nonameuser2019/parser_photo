from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import os

ua = UserAgent()
HEADER = {
    'user-agent': ua.random
}
sub_url = '?page='
sub_dir = 'images/'

def get_html(url):
    html = requests.get(url, headers=HEADER)
    if html.status_code == 200:
        return html
    else:
        print(html.status_code)


def get_photo(src):
    try:
        file_obj = requests.get(src, stream=True)
        return file_obj
    except:
        print("Error src doesn't exists")


def save_image(name, file_obj):
    try:
        with open(name, 'bw')as photo:
            for chunk in file_obj.iter_content(8192):
                photo.write(chunk)
    except AttributeError:
        return print("Photo doesn't writed")


def parser(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    card_list = soup.find_all('div', class_='part_box')
    if len(card_list) > 0:
        for card in card_list:
            dir_name = card.find('div', class_='part_brand').text.replace('/', '')
            art = card.find('div', class_='part_article_id').text.replace('/', '')
            link_img = card.find('div', class_='part_img').find('a', class_='pointer').find('img')['data-src']
            try:
                os.mkdir(sub_dir +dir_name)
            except:
                pass
            save_image(sub_dir + dir_name + '/' + art + '.JPG', get_photo(link_img))
    else:
        return 1


def read_input():
    # читает файл с ссылками на категории
    cat_url_list = []
    with open('input.txt', 'r') as r:
        for line in r:
            cat_url_list.append(line.strip('\n'))
    return cat_url_list


def main():
    url_list = read_input()
    for url in url_list:
        for i in range(1, 5000):
            html = get_html(url + sub_url + str(i))
            print(f'page {i}')
            ret = parser(html)
            if ret == 1:
                break


if __name__ == '__main__':
    main()


