import requests
from bs4 import BeautifulSoup
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


def search_analog(name):
    link = "https://kiberis.ru/data_js.php"
    data = {"fast_search_vvod": name}
    resource = requests.post(link, data=data, headers=header).text
    soup = BeautifulSoup(resource, 'lxml')
    analogAll = soup.findAll("li", {"itemprop": "relatedDrug"})
    result = "🔃Аналоги🔃\n"
    for i in range(len(analogAll)):
        result += "     💊" + " ".join(str(analogAll[i].find('a').text).split()) + "\n"
    return result