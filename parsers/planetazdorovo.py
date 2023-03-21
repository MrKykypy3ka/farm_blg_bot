#TODO  В работе, на сайте стоит система защиты от парсинга
import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


def out(name):
    link = "https://planetazdorovo.ru/search/?q=" + name
    resource = requests.get(link, headers=header)
    c = resource.cookies
    print(list(c.items()))

    resource = requests.get(link, headers=header, cookies=cookies).text
    soup = BeautifulSoup(resource, 'lxml')
    print(resource)
    # priceAll = soup.findAll("div", {"class": "product-card__price "})
    # titleAll = soup.findAll("span", {"itemprop": "name"})
    # arr = {}
    result = "🏥Планета здоровья🏥\n"
    # for i in range(len(titleAll)):
    #     print(titleAll[i].text, "\t", priceAll[i].text)
    #     result += "     💊" + " ".join(str(titleAll[i].find('a').text).split()) + "\n    🪙" + " ".join(str(priceAll[i].find('span').text).split()) + "руб.\n"
        #title =
        #price =
        #arr[title] = price
    #with open("1.html", "w", encoding="utf-8") as file: file.write(block)
    # with open("1.html", "w", encoding="utf-8") as file: file.write(resource)
    return result