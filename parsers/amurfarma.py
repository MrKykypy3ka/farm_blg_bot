import requests
from bs4 import BeautifulSoup
import fake_useragent

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
    name = name.replace("n", "№")
    result = "🏥Амур фармация🏥\n"
    link = "https://www.amurfarma.ru/search/?q=" + name
    resource = requests.get(link, headers=header).text
    soup = BeautifulSoup(resource, 'lxml')
    titleAll = soup.findAll("a", {"class": "name"})
    priceAll = soup.findAll("div", {"class": "basket"})
    for i in range(min(len(titleAll), len(priceAll))):
        result += "     💊" + " ".join(str(titleAll[i].text.lower().replace('мг/мл', 'мг').replace(' введ', '')).split()) + "\n    🪙" + " ".join(str(priceAll[i].text[:priceAll[i].text.index('.')]).split()) + "\n"
    #with open("1.html", "w", encoding="utf-8") as file: file.write(resource)
    return result


def out_min(name):
    name = name.replace("n", "№")
    result = "🏥Амур фармация🏥\n"
    link = "https://www.amurfarma.ru/search/?q=" + name
    resource = requests.get(link, headers=header).text
    soup = BeautifulSoup(resource, 'lxml')
    titleAll = soup.findAll("a", {"class": "name"})
    priceAll = soup.findAll("div", {"class": "basket"})
    price = 100000000.0
    title = ""
    for i in range(min(len(titleAll), len(priceAll))):
        new_price = float(" ".join(str(priceAll[i].text[:priceAll[i].text.index('.')]).split())[:-3].replace(",", "."))
        if new_price < price:
            price = new_price
            title = " ".join(str(titleAll[i].text.lower().replace('мг/мл', 'мг').replace(' введ', '')).split())
    if price != 100000000.0:
        result += "     💊" + title + "\n    🪙" + str(price) + "руб.\n"
    return result


def out_availability(name):
    name = name.replace("n", "№")
    result = "🏥Амур фармация🏥\n"
    link = "https://www.amurfarma.ru/search/?q=" + name
    resource = requests.get(link, headers=header).text
    soup = BeautifulSoup(resource, 'lxml')
    item = soup.findAll("div", {"class": "product_wrap"})
    PRODUCT_ID = ''
    price = 100000000.0
    for i in range(len(item)):
        temp = item[i].find("div", {"class": "basket"})
        new_price = float(" ".join(str(temp.text[:temp.text.index('.')]).split())[:-3].replace(",", "."))
        if new_price < price:
            price = new_price
            datapid = str(item[i])
            PRODUCT_ID = datapid[datapid.index("data-pid=") + 10:datapid.index("data-pid=") + 15]
    link = "https://amurfarma.ru/local/templates/amurfarmacy_2015/ajax.php"
    data = {"ajaxtype": "availability",
            "PRODUCT_ID": PRODUCT_ID}
    resource = requests.post(link, headers=header, data=data).text
    soup = BeautifulSoup(resource, 'lxml')
    h = soup.findAll("div", {"class": "day_wrap"})
    for i in range(len(h)):
        result += h[i].find("h5").text + "\n"
        dragshop = h[i].findAll("div", {"class": "itemm"})
        for j in range(len(dragshop)):
            result += "      " + STREET[dragshop[j].text] + "\n"
    return result