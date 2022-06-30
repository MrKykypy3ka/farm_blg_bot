import json

import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
STREET = {'17155': 'Игнатьевское шоссе, 14/4',
          '14135': 'ул. Амурская, 89',
          '15297': 'ул. Дьяченко, 1/1',
          '15184': 'ул. Зейская, 182',
          '14835': 'ул. Калинина, 82/2',
          '14531': 'ул. Кантемирова, 23',
          '16178': 'ул. Красноармейская, 82',
          '15462': 'ул. Ленина 74',
          '17754': 'ул. Мухина, 10'}


def out(name):
    result = "🏥Миницен🏥\n"
    link = "https://api.minicen.ru/search/main?idTradePoint=15184&Request=" + name + "&SearchType=1&ReturnType=&Sorting=5&idGroup=&Page=1&PerPage=1&idAdvDiscountPage=&dontUseMix=0&idReplacement=&idMNN=&LongSessionID=&ApiVersion=3"
    # data = {'idTradePoint': 15184,
    #         'Request': name,
    #         'SearchType': 1,
    #         'Sorting': 5,
    #         'Page': 1,
    #         'PerPage': 1,
    #         'dontUseMix': 0,
    #         'ApiVersion': 3}
    resource = requests.post(link, headers=header).text
    resource = json.loads(resource)
    for elem in resource['Data']['tovar']:
        if elem['Price'] != None:
            result += "     💊" + str(elem['TovarName']) + "\n    🪙" + str(elem['Price']) + "руб.\n"
    if result == "🏥Миницен🏥\n":
        result += "     ❗️По данному адресу нет этого лекарства, но вы можете посмотреть его в других аптеках.\n"
    return result


def out_min(name):
    result = "🏥Миницен🏥\n"
    link = "https://api.minicen.ru/search/main?idTradePoint=15184&Request=" + name + "&SearchType=1&ReturnType=&Sorting=5&idGroup=&Page=1&PerPage=1&idAdvDiscountPage=&dontUseMix=0&idReplacement=&idMNN=&LongSessionID=&ApiVersion=3"
    # data = {'idTradePoint': 15184,
    #         'Request': name,
    #         'SearchType': 1,
    #         'Sorting': 5,
    #         'Page': 1,
    #         'PerPage': 1,
    #         'dontUseMix': 0,
    #         'ApiVersion': 3}
    resource = requests.post(link, headers=header).text
    resource = json.loads(resource)
    price = 100000000.0
    title = ""
    for elem in resource['Data']['tovar']:
        if elem['Price'] != None:
            if elem['Price'] < price:
                price = elem['Price']
                title = str(elem['TovarName'])
    if price != 100000000.0:
        result += "     💊" + title + "\n    🪙" + str(price) + "руб.\n"
    else:
        result += "     ❗️По данному адресу нет этого лекарства, но вы можете посмотреть его в других аптеках.\n"
    return result


def out_all(name):
    result = ''
    for key in STREET:
        link = "https://api.minicen.ru/search/main?idTradePoint=" + key + "&Request="\
                      + name +\
                      "&SearchType=1&ReturnType=&Sorting=5&idGroup=&Page=1&PerPage=1&idAdvDiscountPage=&dontUseMix=0&idReplacement=&idMNN=&LongSessionID=&ApiVersion=3"
        resource = requests.post(link, headers=header).text
        resource = json.loads(resource)
        result += '🛣' + STREET[key] + '\n'
        for elem in resource['Data']['tovar']:
            if elem['Price'] != None:
                result += "     💊" + str(elem['TovarName']) + "\n    🪙" + str(elem['Price']) + "руб.\n"
    return result


def out_min_all(name):
    result = '🏥Миницен🏥\n'
    for key in STREET:
        price = 100000000.0
        title = ""
        link = "https://api.minicen.ru/search/main?idTradePoint=" + key + "&Request=" \
               + name + \
               "&SearchType=1&ReturnType=&Sorting=5&idGroup=&Page=1&PerPage=1&idAdvDiscountPage=&dontUseMix=0&idReplacement=&idMNN=&LongSessionID=&ApiVersion=3"
        resource = requests.post(link, headers=header).text
        resource = json.loads(resource)
        result += '🛣' + STREET[key] + '\n'
        for elem in resource['Data']['tovar']:
            if elem['Price'] != None:
                if elem['Price'] < price:
                    price = elem['Price']
                    title = str(elem['TovarName'])
        if price != 100000000.0:
            result += "     💊" + title + "\n    🪙" + str(price) + "руб.\n"
    return result


def out_availability(name):
    result = '🏥Миницен🏥\n'
    for key in STREET:
        link = "https://api.minicen.ru/search/main?idTradePoint=" + key + "&Request=" \
               + name + \
               "&SearchType=1&ReturnType=&Sorting=5&idGroup=&Page=1&PerPage=1&idAdvDiscountPage=&dontUseMix=0&idReplacement=&idMNN=&LongSessionID=&ApiVersion=3"
        resource = requests.post(link, headers=header).text
        resource = json.loads(resource)
        price = 100000000.0
        title = ""
        for elem in resource['Data']['tovar']:
            if elem['Price'] != None:
                if elem['Price'] < price:
                    price = elem['Price']
        if price != 100000000.0:
            result += STREET[key] + '\n'
    return result