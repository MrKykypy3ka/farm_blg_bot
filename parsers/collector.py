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
    try:
        return analog.search_analog(name)
    except:
        return "🏥Аналоги🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"


def print_availability(name, dragshop):
    try:
        if dragshop == 'Твоя аптека':
            return tvoyaApteka.out_availability(name)
    except:
        return "🏥Твоя аптека🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        if dragshop == 'Миницен':
            return minicen.out_availability(name)
    except:
        return "🏥Миницен🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        if dragshop == 'Монастырёв':
            return monastirev.out_availability(name)
    except:
        return "🏥Монастырёв🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"
    try:
        if dragshop == 'Амур Фармация':
             return amurfarma.out_availability(name)
    except:
        return "🏥Амур Фармация🏥\n😔Ошибка поиска (в скором времени мы всё поправим)"


def print_minicen(name, choise):
    try:
        if choise == 'all':
            return minicen.out_all(name)
        else:
            return minicen.out_min_all(name)
    except:
        return "😔Ошибка поиска (в скором времени мы всё поправим)"