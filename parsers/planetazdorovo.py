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
    cookies = {'_dc_gtm_UA-126829878-1': "1",
               '_ga': "GA1.2.1932622488.1648288266",
               '_gcl_au': "1.1.850368603.1648288261",
               '_gid': "GA1.2.1168798475.1648986989",
               '_ym_d': "1648288266",
               '_ym_isad': "1",
               '_ym_uid': "1648288266331015266",
               '_ym_visorc': "b",
               'BITRIX_CONVERSION_CONTEXT_s1': "{\"ID\":4,\"EXPIRE\":1649012340,\"UNIQUE\":[\"conversion_visit_day\"]}",
               'BX_USER_ID': "0fced4eeaaa3402001bd320cbc028c3a",
               'carrotquest_auth_token': "user.1142362913252575398.23139-c082d1441dfd0f22105416f38a.fcf760ff69c00693c8010c5d6b31ed621f44c0361827430a",
               'carrotquest_device_guid': "22a08243-1e14-41db-a6fc-8476f9a98b35",
               'carrotquest_realtime_services_transport': "wss",
               'carrotquest_session': "ivxnhu1h09mnjc18kgvt3gleq0tx4eki",
               'carrotquest_session_started': "1",
               'carrotquest_uid': "1142362913252575398",
               'city': "Ð\u0091Ð»Ð°Ð³Ð¾Ð²ÐµÑ\u0089ÐµÐ½Ñ\u0081Ðº",
               'city_code': "blagoveshhensk",
               'city_id': "1107313",
               'city_xml': "596",
               'help_phone': "(4162) 51-44-44",
               'hide_footer_fixed': "1",
               'IS_CITY_CHANGE': "1",
               'is_order_warning': "1",
               'order_phone': "8-800-755-00-77",
               'PHPSESSID': "2iTXPTp3weuwdlN3Tc16nBexZNaI8wJf",
               'qrator_jsid': "1648986977.873.wiPHiu7XKv7EDCn3-1l19djs6hf57clcsbduli8758llhgt3k",
               'qrator_jsr': list(c.items())[0][1],
               'qrator_ssid': "1648986978.647.4bfMSigN2ezmRPna-q6k3p7apgcj2a09var595nmis6e3m1tn",
               'region': "51",
               'region_id': "12",
               'show_bonus': "1",
               'timezone': "32400",
               'tmr_detect': "1|1648989104046",
               'tmr_lvid': "bbbe7cad29cce50ff7607aa5648bf768",
               'tmr_lvidTS': "1648288265470",
               'tmr_reqNum': "154"}
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