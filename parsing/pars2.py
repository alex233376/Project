from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


class Content:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }


html = urlopen("https://www.avito.ru/petrozavodsk/nastolnye_kompyutery")
bsObj = BeautifulSoup(html, "lxml")
nameList = bsObj.findAll("div", {"class": "description item_table-description"})
for name in nameList:
    print(name.get_text(strip=True))
# "http://www.pythonscraping.com/pages/page3.html"
# https://www.avito.ru/petrozavodsk/nastolnye_kompyutery
