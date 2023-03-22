import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


def out(name):
    result = "🏥Твоя Аптека🏥\n"
    link = "https://www.tvoyaapteka.ru/auth/?auth=1"
    data = {'ajax_call': "y",
            'INPUT_ID':	"title-search-input",
            'q': name,
            'l': "3",
            'sid': "f415"}
    resource = requests.post(link, data=data, headers=header).text
    soup = BeautifulSoup(resource, 'lxml')
    priceAll = soup.findAll("div", {"class": "price_2 hidden-spp-store"})
    titleAll = soup.findAll("div", {"class": "title"})
    if len(priceAll) == 0:
        result += "Такого товара нет\n"
        return result
    for i in range(len(priceAll)):
        result += "     💊" + " ".join(str(titleAll[i].find('a').text).split())\
                  + "\n    🪙" + " ".join(str(priceAll[i].find('span').text).split()) + "руб.\n"
    return result

def out_min(name):
    link = "https://www.tvoyaapteka.ru/auth/?auth=1"
    data = {'ajax_call': "y",
            'INPUT_ID':	"title-search-input",
            'q': name,
            'l': "3",
            'sid': "f415"}
    resource = requests.post(link, data=data, headers=header).text
    soup = BeautifulSoup(resource, 'lxml')
    priceAll = soup.findAll("div", {"class": "price_2 hidden-spp-store"})
    titleAll = soup.findAll("div", {"class": "title"})
    result = "🏥Твоя Аптека🏥\n"
    price = 100000000.0
    title = ""
    if len(priceAll) == 0:
        result += "Такого товара нет\n"
    for i in range(len(priceAll)):
        new_price = float("".join(str(priceAll[i].find('span').text).split()).replace(",", "."))
        if new_price < price:
            price = new_price
            title = " ".join(str(titleAll[i].find('a').text).split())
    if price != 100000000.0:
        result += "     💊" + title + "\n    🪙" + str(price) + "руб.\n"
    return result


def out_availability(name):
    link = "https://www.tvoyaapteka.ru/auth/?auth=1"
    data = {'ajax_call': "y",
            'INPUT_ID':	"title-search-input",
            'q': name,
            'l': "3",
            'sid': "f415"}
    resource = requests.post(link, data=data, headers=header).text
    soup = BeautifulSoup(resource, 'lxml')
    item = soup.findAll("div", {"class": "bx_item_block clearfix"})
    availability = ''
    result = "🏥Твоя Аптека🏥\n"
    price = 9000000
    for i in range(len(item)):
        if float("".join(str(item[i].find("div", {"class": "price_2 hidden-spp-store"}).find("span").text).split()).replace(",", ".")) < price:
            availability = ''
            item_availability = item[i].find("select", {"class": "item_store_select validate[required]"}).findAll("option", {"class": ""})
            for j in range(len(item_availability)):
                availability += item_availability[j].text + "\n"
    result += availability.replace(", посмотрите все", "").replace("Доставка", "").replace("  ", "").replace("\n\n", "\n")
    return result
