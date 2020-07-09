import requests
from bs4 import BeautifulSoup

url = 'https://www.avito.ru/petrozavodsk/nastolnye_kompyutery'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
HOST = 'https://www.avito.ru'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='pagination-page')
    if pagination:
        return pagination[-1].get_text()
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # получаем блоки объявлений
    items = soup.find_all('div', class_='item__line')
    cars = []
    for item in items:
        cars.append({
            'title': item.find('div', class_='snippet-title-row').get_text(strip=True),
            'link': HOST + item.find('a', class_='snippet-link').get('href'),
            'usd_prise': item.find('span', class_='snippet-price').get_text().replace('\n', ''),
            'cyti': item.find('span', class_='item-address-georeferences-item__content').get_text(),
        })
    return cars


def parse():
    html = get_html(url)
    if html.status_code == 200:
        pages_count = get_pages_count(html.text)
        print(pages_count)
        # cars = get_content(html.text)

    else:
        print('Ошибка')


parse()
# https://www.avito.ru/petrozavodsk/planshety_i_elektronnye_knigi?cd=1
# https://www.avito.ru/petrozavodsk/nastolnye_kompyutery
