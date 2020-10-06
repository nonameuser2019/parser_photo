from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import os

ua = UserAgent()
HEADER = {
    'user-agent': ua.random
}
main_url = input('Enter link ') + '?page='


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


def get_page_count(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    count = soup.find('ul', class_='pagination').find_all('li')[-1].find('a')['href']
    page_cout = count.find('page=')
    return count[page_cout + 5:]


def parser(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    card_list = soup.find_all('div', class_='product-layout')
    for card in card_list:
        img = card.find('picture').find('img')['src'].strip()
        art = card.find('picture').find('img')['alt'].replace('/', '')
        try:
            brand_str = card.find('div', class_='man_image').find('img')['data-tip']
            dir_name = brand_str[brand_str.find('-') + 1:]
        except:
            dir_name = 'other'
        try:
            os.mkdir(dir_name)
        except:
            print(f'{dir_name} already exists')
        try:
            save_image(dir_name + '/' + art + '.JPG', get_photo(img))
        except:
            print(f'Error {art}')

def main():
    page_count = get_page_count(get_html(main_url))
    for count in range(1, int(page_count) + 1):
        parser(get_html(main_url + str(count)))
        print(f'{count} / {page_count}')



if __name__ == '__main__':
    main()
