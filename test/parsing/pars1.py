from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, 'html.parser')
# функция findAll создает список слов привязаных к span class green
nameList = bsObj.findAll("span", {"class":"green"})
# можно вывести сразу несколько совпадени по тегам
# nameList = bsObj.findAll("span", {"class":["green", "red"]})
for name in nameList:
    print(name.get_text())
# get_text() удаляет все теги и печатает только текст