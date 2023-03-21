from parsers import tvoyaApteka
from parsers import minicen
from parsers import aptekaru
from parsers import amurfarma
from parsers import monastirev
from parsers import planetazdorovo
from parsers import analog


def print_price(name):
    result = ""
    try:
        result += tvoyaApteka.out(name)
    except:
        result += "🏥Твоя Аптека🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += monastirev.out(name)
    except:
        result += "🏥Монастырёв🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += aptekaru.out(name)
    except:
        result += "🏥Аптека.Ру🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += minicen.out(name)
    except:
        result += "🏥Миницен🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += amurfarma.out(name)
    except:
        result += "🏥Амурфармация🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    return result


def print_min_price(name):
    result = ""
    try:
        result += tvoyaApteka.out_min(name)
    except:
        result += "🏥Твоя Аптека🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += monastirev.out_min(name)
    except:
        result += "🏥Монастырёв🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += aptekaru.out_min(name)
    except:
        result += "🏥Аптека.Ру🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += minicen.out_min(name)
    except:
        result += "🏥Миницен🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        result += amurfarma.out_min(name)
    except:
        result += "🏥Амурфармация🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    return result


def print_analog(name):
    return analog.search_analog(name)


def print_availability(name, dragshop):
    if dragshop == 'Твоя аптека':
        return tvoyaApteka.out_availability(name)
    elif dragshop == 'Миницен':
        return minicen.out_availability(name)
    elif dragshop == 'Монастырёв':
        return monastirev.out_availability(name)
    # elif dragshop == 'Амур Фармация':
    #     return amurfarma.out_availability(name)


def print_minicen(name, choise):
    if choise == 'all':
        return minicen.out_all(name)
    else:
        return minicen.out_min_all(name)
