from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json


#cat_url = input('Enter category url')
main_url = 'https://webshop-ua.intercars.eu/'
cat_url = 'https://webshop-ua.intercars.eu/zapchasti/shassi-6300000&manufacturers=555&avail=0&onoffer=0&page='
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
    page_list = soup.find('ul', class_='gc-pagination').find_all('li', class_='page-item')[-1].text.strip()
    return page_list


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
    card_list = soup.find_all('div', class_='baner-container-B2C')
    for card in card_list:
        name = card.find('a', class_='fullcard').find('h3').find('span').text
        src = soup.find('div', class_='art-images margincenter').find('a')['data-dyngalposstring']
        lnk =



def main():
    count = parser(get_html(cat_url))



if __name__ == '__main__':
    main()
