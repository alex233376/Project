# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.avito.ru/petrozavodsk/nastolnye_kompyutery'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://www.avito.ru'
FILE = 'tovar.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='pagination-page')
    if pagination:
        return int(pagination[-2].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # получаем блоки объявлений
    items = soup.find_all('div', class_='item__line')
    tovar = []
    for item in items:
        tovar.append({
            'title': item.find('div', class_='snippet-title-row').get_text(strip=True),
            'link': HOST + item.find('a', class_='snippet-link').get('href'),
            'usd_prise': item.find('span', class_='snippet-price').get_text().replace('\n', ''),
            'cyti': item.find('div', class_='item-address-georeferences').get_text(),
        })
    return tovar


def save_file(items, path):
    with open(path, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название', 'Ссылка', 'Цена', 'Город'])
        for item in items:
            writer.writerow([item['title'], item['link'],
                             item['usd_prise'], item['cyti']])


def parse():
    url = input('Введите адрес...')
    url = url.strip()
    html = get_html(url)
    if html.status_code == 200:
        tovar = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(url, params={'page': page})
            get_content(html.text)
            tovar.extend(get_content(html.text))
        save_file(tovar, FILE)
        print(f'Получено {len(tovar)} товара')
    else:
        print('Ошибка')


parse()
