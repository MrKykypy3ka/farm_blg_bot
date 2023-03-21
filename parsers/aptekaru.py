import json
import requests
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


def out(name):
    link = "https://api.apteka.ru/Search/ByPhrase?pageSize=25&page=0&iPharmTownId=&withprice=false&withprofit=false&withpromovits=false&phrase=" + name + "&cityId=5e6b6427cea9880001078370"
    data = {'pageSize': '25',
            'page': '0',
            'withprice': 'false',
            'withprofit': 'false',
            'withpromovits': 'false',
            'phrase': name,
            'cityId': '5e6b6427cea9880001078370'}
    resource = requests.get(link, data=data, headers=header).text
    resource = json.loads(resource)
    result = "🏥Аптека.РУ🏥\n"
    if 'result' not in resource:
        return result
    for key in resource['result']:
        if float(key['minPrice']) != 0:
            result += "     💊" + str(key['tradeName']).replace('</em>', '').replace('<em>', '') + "\n    🪙" + str(key['minPrice']) + "руб.\n"
    return result


def out_min(name):
    link = "https://api.apteka.ru/Search/ByPhrase?pageSize=25&page=0&iPharmTownId=&withprice=false&withprofit=false&withpromovits=false&phrase=" + name + "&cityId=5e6b6427cea9880001078370"
    data = {'pageSize': '25',
            'page': '0',
            'withprice': 'false',
            'withprofit': 'false',
            'withpromovits': 'false',
            'phrase': name,
            'cityId': '5e6b6427cea9880001078370'}
    resource = requests.get(link, data=data, headers=header).text
    resource = json.loads(resource)
    result = "🏥Аптека.РУ🏥\n"
    price = 100000000.0
    title = ""
    if 'result' not in resource:
        return result
    for key in resource['result']:
        if float(key['minPrice']) < price and float(key['minPrice']) != 0:
            price = float(key['minPrice'])
            title = str(key['tradeName']).replace('</em>', '').replace('<em>', '')
    if price != 100000000.0:
        result += "     💊" + title + "\n    🪙" + str(price) + "руб.\n"
    return result