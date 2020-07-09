from collections import namedtuple

import bs4
import requests

InnerBlock = namedtuple('Block', 'title,price,currency,date,url')


class AvitoParser:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }

    def get_page(self, page: int = None):
        params = {
            'radius': 0,
            'user': 1,
        }
        if page and page > 1:
            params['p'] = page
        url = 'https://www.avito.ru/petrozavodsk/nastolnye_kompyutery'
        r = self.session.get(url, params=params)
        return r.text

    def parse_block(self, item):
        url_block = item.select_one('a.snippet-link')
        href = url_block.get('href')
        if href:
            url= 'https://www.avito.ru' + href
        else:
            url = None
        title_block = item.select_one('h3.title')
        print(title_block)
        return

    def get_blocks(self):
        text = self.get_page(page=2)
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('div', class_='item__line')
        for item in container:
            block = self.parse_block(item=item)
            return
            print(block)


def main():
    p = AvitoParser()
    p.get_blocks()


if __name__ == '__main__':
    main()
