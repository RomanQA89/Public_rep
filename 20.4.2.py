# Задание на автоматизацию проверки ответа API от сервера.
# Тест проверяет JSON файлы на правильность полей.

import json

name = input('Введите название файла json: ')

with open(name, encoding='utf8') as f:  # Открытие файла для чтения и последующего его закрытия для экономии памяти.
    templates = json.load(f)            # Преобразование файла json в словарь.

def CheckInt(item):                     # Функция для проверки наличия типа int в ключах словаря.
    return type(item) == int

def CheckStr(item):                     # Функция для проверки наличия типа str в ключах словаря.
    return type(item) == str

def CheckBool(item):                    # Функция для проверки наличия типа bool в ключах словаря.
    return type(item) == bool

def CheckUrl(item):                     # Функция для проверки наличия типа str в ключах словаря.
    if type(item) == str:
        return item.startswith('http://') or item.startswith('https://')  # Функция .startswith проверяет наличие http:// или https:// в начале строки.
    else:
        return False

def CheckStrValue(item, val):          # Функция для проверки наличия типа str со значениями itemBuyEvent или itemViewEvent в ключах словаря.
    if type(item) == str:
        return item in val
    else:
        return False

def ErrorLog(keys, value, string):     # Функция для добавления возможных ошибок в отдельный список.
    Error.append({keys: f'{value}, {string}'})

# Список требований к ответу API от сервера.
listofItems = {'timestamp': 'int', 'referer': 'url', 'location': 'url', 'remoteHost': 'str', 'partyId': 'str',
               'sessionId': 'str', 'pageViewId': 'str', 'eventType': 'val', 'item_id': 'str', 'item_price': 'int',
               'item_url': 'url', 'basket_price': 'str', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool',
               'firstInSession': 'bool', 'userAgentName': 'str'}

Error = []
for dict in templates:               # Проходимся по всему словарю.
    for keys in dict:                # Проходимся по ключам (переменным) словаря.
        if keys in listofItems:
            if listofItems[keys] == 'int':
                if not CheckInt(dict[keys]):
                    ErrorLog(keys, dict[keys], f'ожидали тип {listofItems[keys]}')
            elif listofItems[keys] == 'str':
                if not CheckStr(dict[keys]):
                    ErrorLog(keys, dict[keys], f'ожидали тип {listofItems[keys]}')
            elif listofItems[keys] == 'bool':
                if not CheckBool(dict[keys]):
                    ErrorLog(keys, dict[keys], f'ожидали тип {listofItems[keys]}')
            elif listofItems[keys] == 'url':
                if not CheckUrl(dict[keys]):
                    ErrorLog(keys, dict[keys], f'ожидали тип {listofItems[keys]}')
            elif listofItems[keys] == 'val':
                if not CheckStrValue(dict[keys], ['itemBuyEvent', 'itemViewEvent']):
                    ErrorLog(keys, dict[keys], 'ожидали значение itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(keys, dict[keys], 'неожиданное значение')
        else:
            ErrorLog(keys, dict[keys], 'неизвестная переменная')
if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)

