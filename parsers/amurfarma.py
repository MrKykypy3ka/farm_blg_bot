from bs4 import BeautifulSoup
import fake_useragent
from selenium import webdriver

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
STREET = {'1': 'ул. Комсомольская, д. 3',
          '2': 'ул. Политехническая, д. 55',
          '3': 'ул. Текстильная, д. 33, пом. 1-9',
          '22': 'ул. 50 лет Октября, д.42/1',
          '41': 'п. Моховая Падь, литер 25/1',
          '42': 'ул. Зейская, д.88, пом.III',
          '45': 'ул. Пионерская, д.33',
          '48': 'ул. Театральная, д.236',
          '50': 'ул. Нагорная, д.1',
          '51': 'ул. Ленина, д. 29/37',
          '78': 'ул. Воронкова, д.26',
          '78/1': 'ул. Воронкова, д.26/3 ',
          '80': 'ул. Калинина, д.84 литер Б',
          '81': 'ул. Студенческая, д.38',
          '83': 'ул. Пионерская, д.14, литер А',
          '101': 'ул. Институтская/Калинина, д.1/140',
          '105': 'ул. Мухина, д.114',
          '106': 'ул. Тенистая, 160',
          '107': 'Игнатьевское шоссе, 10/4',
          '108': 'ул. Амурская, 201А',
          '115': 'ул. Шимановского, 38'}

def out(name):
    result = "🏥Амур фармация🏥\n"
    driver = webdriver.Chrome()
    driver.get("https://amurfarma.ru/search/?q=" + name)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    titleAll = soup.findAll("h5", {"class": "h5 catalog-item__name"})
    priceAll = soup.findAll("div", {"class": "catalog-item__old-price"})
    for i in range(len(titleAll)):
        title = str(titleAll[i]).replace('<h5 class="h5 catalog-item__name"><strong>', '').replace('</strong>',
                                                                                                   '').replace('</h5>',
                                                                                                               '')
        price = str(priceAll[i]).replace('''<div class="catalog-item__old-price">
                Цена без скидки:
                <span class="price">''', '').replace('</span></div>', '')
        result += "     💊" + title + "\n     🪙" + price + "\n"
    return result


def out_min(name):
    result = "🏥Амур фармация🏥\n"
    driver = webdriver.Chrome()
    driver.get("https://amurfarma.ru/search/?q=" + name)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    titleAll = soup.findAll("h5", {"class": "h5 catalog-item__name"})
    priceAll = soup.findAll("div", {"class": "catalog-item__old-price"})
    minPrice = 1000000
    minTital = ""
    for i in range(len(titleAll)):
        title = str(titleAll[i]).replace('<h5 class="h5 catalog-item__name"><strong>', '').replace('</strong>',
                                                                                                   '').replace('</h5>',
                                                                                                               '')
        price = str(priceAll[i]).replace('''<div class="catalog-item__old-price">
                Цена без скидки:
                <span class="price">''', '').replace('</span></div>', '')
        if minPrice >= int(price[:-2]):
            minPrice = int(price[:-2])
            minTital = title
    result += "     💊" + minTital + "\n     🪙" + str(minPrice) + "р.\n"
    return result


def out_availability(name):
    result = "🏥Амур фармация🏥\n"
    driver = webdriver.Chrome()
    driver.get("https://amurfarma.ru/search/?q=" + name)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    titleAll = soup.findAll("h5", {"class": "h5 catalog-item__name"})
    priceAll = soup.findAll("div", {"class": "catalog-item__old-price"})
    minPrice = 1000000
    minTital = ""
    for i in range(len(titleAll)):
        price = str(priceAll[i]).replace('''<div class="catalog-item__old-price">
                    Цена без скидки:
                    <span class="price">''', '').replace('</span></div>', '')
        if minPrice >= int(price[:-2]):
            minPrice = int(price[:-2])
            minTital = str(titleAll[i]).replace('<h5 class="h5 catalog-item__name"><strong>', '').replace('</strong>',
                                                                                                   '').replace('</h5>',
                                                                                                               '')
            availabilityAll = soup.findAll("div", {"class": "link link--no-dash in-stock__item"})
    result += "     💊" + minTital + "\n     🪙" + str(minPrice) + "р.\n"
    return result
