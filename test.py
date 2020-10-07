from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import json



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
        print('.I.')


file_obj = get_photo('https://static.iauto.by/images/1/00019199903255.jpg')
print(file_obj)
save_image('test.JPG', file_obj)