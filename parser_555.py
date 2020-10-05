from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json


main_url = 'https://555parts.ru/555?page='
sub_url_img = '-500x500.jpg'
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


def get_page_count(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    page = soup.find('ul', class_='pagination').find_all('li')[-1].find('a')['href']
    page_count = page[page.find('=')+1:]
    return page_count



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
        print("Photo doesn't writed")


def parser(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    card_list = soup.find_all('div', class_='product-layout product-list')
    for card in card_list:
        art = card.find('span', class_='code').find('span').text
        full_href = card.find('div', class_='image').find('a').find('img')['src']
        if full_href != 'https://555parts.ru/image/cache/no_image-100x100.png':
            href = full_href[:full_href.rfind('-')]
            file_obj = get_photo(href + sub_url_img)
            save_image('555/'+ art + '.JPG', file_obj)



def main():
    page_count = get_page_count(get_html('https://555parts.ru/555'))
    for cnt in range(1, int(page_count)+1):
        parser(get_html(main_url + str(cnt)))
        print(f'{cnt}/{page_count}')



if __name__ == '__main__':
    main()