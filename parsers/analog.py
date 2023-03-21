import requests
from bs4 import BeautifulSoup
import fake_useragent
from transliterate import translit


def search_analog(name):
    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}

    link = f"https://analogi.info/{translit(name, language_code='ru', reversed=True)}"
    resource = requests.post(link, headers=header).text

    soup = BeautifulSoup(resource, 'lxml')
    analogAll = soup.findAll("td")
    count = 0
    result = "🔃Аналоги🔃\n"
    for i in range(len(analogAll)):
        td = str(analogAll[i])
        if td.find('href="https://analogi.info/') > -1:
            count += 1
            result += "     💊" + td[td.find(">", 20) + 1:td.find("<", 20)] + "\n"
        if count == 10:
            break
    return result
