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



def read_input():
    # читает файл с ссылками на категории
    cat_url_list = []
    with open('input.txt', 'r') as r:
        for line in r:
            cat_url_list.append(line.strip('\n'))
    return cat_url_list


def get_page_count(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    page_count = soup.find('div' ,class_='paging').text
    return int(page_count[page_count.find('из ') + 3:])


def parser(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    card_list = soup.find_all('div', class_='part-item-view')
    for card in card_list:
        brand = card.find('div', class_='part-name').find('a').text
        brand_list = brand.split('\n')
        dir_name = brand_list[1].strip('\t').strip()
        art = brand_list[2].strip('\t').strip().replace('/', '')
        try:
            os.mkdir(sub_dir + dir_name)
        except:
            pass
        link_img = card.find('div', class_='part-photo').find('a').find('img')['data-src']
        logo = link_img.find('logos')
        if logo == -1:
            save_image(sub_dir + dir_name + '/' + art + '.JPG', get_photo(link_img))


def main():
    url_list = read_input()
    for url in url_list:
        html = get_html(url)
        page_count = get_page_count(get_html(url))
        for count in range(1, page_count):
            parser(get_html(url + sub_url + str(count)))
            print(f'{count} / {page_count}')


if __name__ == '__main__':
    main()
