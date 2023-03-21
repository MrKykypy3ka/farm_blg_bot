import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
trash = ['ампула темного стекла в упаковке контурной пластиковой (поддоны)',
         'упаковка контурная ячейковая',
         'покрытые пленочной оболочкой',
         'для приготовления раствора для приема внутрь',
         'пакет из комбинированного материала',
         'пакет цефленовый',
         'флакон с распылительной системой',
         'флакон полимерный с распылителем',
         'флакон пластиковый с распылителем',
         'флакон пластиковый с распылителем',
         'флакон',
         'флакон-капельница']


def out(name):
    result = "🏥Монастырёв🏥\n"
    name = name.replace("n", "№")
    link = "https://monastirev.ru/search?term=" + name
    cookies = {'kladr': '2800000100000'}
    resource = requests.post(link, headers=header, cookies=cookies).text
    soup = BeautifulSoup(resource, 'lxml')
    soup = soup.find('div', {'class': 'listing'})
    item = soup.findAll("div", {"class": "offer js-assortment-unit-show"})
    for elem in item:
        title = elem.find('div', {'class': 'offer__title link__text'}).text
        title = " ".join(str(title.lower()).split())
        dosage = elem.find('div', {'class': 'offer__description'}).text
        dosage = " ".join(str(dosage.lower()).split())
        dosage = dosage\
            .replace('внутривенного введения', 'в/в')\
            .replace('внутримышечного введения', 'в/м')\
            .replace('раствор', 'р-р')\
            .replace('таблетки', 'тбл')\
            .replace('ампула', 'амп')
        price = elem.findAll('div', {'class': 'offer__price-block'})
        result += "     💊" + title + ' ' + dosage + '\n'
        if len(price) == 0:
            date = elem.find('div', {'class': 'offer__historycal-date'}).text
            date = " ".join(str(date.lower()).split())
            price_now = elem.find('div', {'class': 'offer__price-current'}).text
            price_now = " ".join(str(price_now.lower()).replace(" ", "").split()) + 'руб.'
            result += "    🪙" + date + price_now + '\n'
        elif 'offer__price-unavailable' in str(price[0]):
            date_fut = price[1].find('div', {'class': 'offer__price-block-header'}).text
            date_fut = " ".join(str(date_fut.lower()).split())
            price_fut = price[1].find('div', {'class': 'offer__price-current'}).text
            price_fut = " ".join(str(price_fut.lower()).replace(" ", "").split()) + 'руб.'
            result += "    🪙" + date_fut + ': ' + price_fut + '\n'
        elif 'offer__price-unavailable' in str(price[1]):
            date_now = price[0].find('div', {'class': 'offer__price-block-header'}).text
            date_now = " ".join(str(date_now.lower()).split())
            price_now = price[0].find('div', {'class': 'offer__price-current'}).text
            price_now = " ".join(str(price_now.lower()).replace(" ", "").split()) + 'руб.'
            result += "    🪙" + date_now + ' ' + price_now + '\n'
        else:
            date_now = price[0].find('div', {'class': 'offer__price-block-header'}).text
            date_now = " ".join(str(date_now.lower()).split())
            price_now = price[0].find('div', {'class': 'offer__price-current'}).text
            price_now = " ".join(str(price_now.lower()).replace(" ", "").split()) + 'руб.'
            date_fut = price[1].find('div', {'class': 'offer__price-block-header'}).text
            date_fut = " ".join(str(date_fut.lower()).split())
            price_fut = price[1].find('div', {'class': 'offer__price-current'}).text
            price_fut = " ".join(str(price_fut.lower()).split()) + 'руб.'
            result += "    🪙" + date_now + ' ' + price_now + '\n' + "    🪙" + date_fut + ': ' + price_fut + '\n'
    return result


def out_min(name):
    result = ''
    name = name.replace("n", "№")
    price_temp = 1000000.0
    date_now_temp = ""
    date_fut_temp = ""
    price_fut_temp = ""
    link = "https://monastirev.ru/search?term=" + name
    cookies = {'kladr': '2800000100000'}
    resource = requests.post(link, headers=header, cookies=cookies).text
    soup = BeautifulSoup(resource, 'lxml')
    soup = soup.find('div', {'class': 'listing'})
    item = soup.findAll("div", {"class": "offer js-assortment-unit-show"})
    for elem in item:
        title = elem.find('div', {'class': 'offer__title link__text'}).text
        title = " ".join(str(title.lower()).split())
        dosage = elem.find('div', {'class': 'offer__description'}).text
        dosage = " ".join(str(dosage.lower()).split())
        dosage = dosage \
            .replace('внутривенного введения', 'в/в') \
            .replace('внутримышечного введения', 'в/м') \
            .replace('раствор', 'р-р') \
            .replace('таблетки', 'тбл') \
            .replace('ампула', 'амп')
        price = elem.findAll('div', {'class': 'offer__price-block'})
        if len(price) == 0:
            continue
        elif 'offer__price-unavailable' in str(price[0]):
            price_fut = price[1].find('div', {'class': 'offer__price-current'}).text
            price_fut = float(" ".join(str(price_fut.lower()).replace(" ", "").split()))
            if price_fut < price_temp:
                result = "🏥Монастырёв🏥\n" + "     💊" + title + ' ' + dosage + '\n'
                price_temp = price_fut
                date_now_temp = price[1].find('div', {'class': 'offer__price-block-header'}).text
                date_now_temp = " ".join(str(date_now_temp.lower()).split())
        elif 'offer__price-unavailable' in str(price[1]):
            price_now = price[0].find('div', {'class': 'offer__price-current'}).text
            price_now = float(" ".join(str(price_now.lower()).replace(" ", "").split()))
            if price_now < price_temp:
                result = "🏥Монастырёв🏥\n" + "     💊" + title + ' ' + dosage + '\n'
                date_now_temp = price[0].find('div', {'class': 'offer__price-block-header'}).text
                date_now_temp = " ".join(str(date_now_temp.lower()).split())
                price_temp = price_now
        else:
            price_now = price[0].find('div', {'class': 'offer__price-current'}).text
            price_now = float(" ".join(str(price_now.lower()).replace(" ", "").split()))
            if price_now < price_temp:
                result = "🏥Монастырёв🏥\n" + "     💊" + title + ' ' + dosage + '\n'
                date_now_temp = price[0].find('div', {'class': 'offer__price-block-header'}).text
                date_now_temp = " ".join(str(date_now_temp.lower()).split())
                date_fut_temp = price[1].find('div', {'class': 'offer__price-block-header'}).text
                date_fut_temp = " ".join(str(date_fut_temp.lower()).split())
                price_fut_temp = price[1].find('div', {'class': 'offer__price-current'}).text
                price_fut_temp = " ".join(str(price_fut_temp.lower()).split()) + 'руб.'
                price_temp = price_now
    if price_temp != 1000000.0:
        result += "    🪙" + date_now_temp + ' ' + str(price_temp) + 'руб.' + '\n' + "    🪙" + date_fut_temp + ': ' + price_fut_temp + '\n'
    else:
        result = "🏥Монастырёв🏥\n"
    return result

def out_availability(name):
    result = "🏥Монастырёв🏥\n"
    link = "https://monastirev.ru/search?term=" + name
    cookies = {'kladr': '2800000100000'}
    resource = requests.post(link, headers=header, cookies=cookies).text
    soup = BeautifulSoup(resource, 'lxml')
    item = soup.findAll("div", {"data-viewport-type": "list"})
    availability = ''
    price = 100000000.0
    for i in range(len(item)):
        if float("".join(item[i].find("div", {"class": "offer__price-current"}).text.split())) < price:
            availability = item[i].find("div", {"class": "preferred-trade-point-block__name flex text-bold"}).text
    result += availability
    return result