from parsers import tvoyaApteka
from parsers import minicen
from parsers import aptekaru
from parsers import amurfarma
from parsers import monastirev
from parsers import planetazdorovo
from parsers import analog


def print_price(name):
    result = tvoyaApteka.out(name)\
              + minicen.out(name)\
              + monastirev.out(name)\
              + aptekaru.out(name)
              # + amurfarma.out(name)
    return result


def print_min_price(name):
     result = tvoyaApteka.out_min(name)\
              + minicen.out_min(name)\
              + monastirev.out_min(name)\
              + aptekaru.out_min(name)

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