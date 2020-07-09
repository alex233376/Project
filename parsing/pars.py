from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


class Content:
    def __init__(self, url, title, body):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }
        self.url = url
        self.title = title
        self.body = body


def get_page(url):
    req = requests.get(url)
    if req.status_code == 200:
        return BeautifulSoup(req.text, 'lxml')
    return None


def news_from_lenta(url):
    bs = get_page(url)
    if bs is None:
        return bs
    title = bs.find('h1', {'class': 'b-topic__title'}).text
    lines = bs.find_all('p')
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)


content = news_from_lenta('https://lenta.ru/news/2020/07/02/odobrili/')
if content is None:
    print('Ошибка')
else:
    print('Заголовок: {}'.format(content.title))
    print('Адрес: {}'.format(content.url))
    print(content.body)
