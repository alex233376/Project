from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.avito.ru/kareliya/audio_i_video/televizory_i_proektory-ASgBAgICAUSIArgJ?cd=1')
bsObj = BeautifulSoup(html)
nameLiist = bsObj.find_all('div', {'class': 'snippet-list'})
for name in nameLiist:
    print(name.get_text())
