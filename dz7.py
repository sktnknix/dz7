# -*- coding: utf-8 -*-

cook_book = {}
_file = open('recipe.txt', 'r')
_list_from_file = []
_dish = []
from re import fullmatch
pattern = r'\d\.\d+'
while 1:
    line = _file.readline()
    if not line:
        _list_from_file.append(_dish)
        break
    elif line == '\n':
        _list_from_file.append(_dish)
        _dish = []
    elif not line.strip('\n').isnumeric():
        if '|' in line:
            line = line.strip('\n').split(' | ')
            _ingr = {}
            _ingr['ingridient_name'] = line[0]
            if line[1].isdigit():
                _ingr['quantity'] = int(line[1])
            elif fullmatch(pattern, line[1]):
                _ingr['quantity'] = float(line[1])
            _ingr['measure'] = line[2]
            _dish.append(_ingr)
        else:
            _dish.append(line.strip('\n'))

for _list in _list_from_file:
    cook_book[_list[0]] = [values for values in _list[1:]]

for keys, values in cook_book.items():
    print(keys + ': ' + str(values))

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    if ',' in dishes:
        _list = dishes.split(', ')
    else:
        _list = [dishes]
    for dish in _list:
        if dish not in cook_book.keys():
            print('Блюда ' + dish + ' нет в наличии')
        else:
            for ingr in cook_book[dish]:
                if not ingr['ingridient_name'] in result:
                    result.update({ingr['ingridient_name']: {'measure': ingr['measure'], 'quantity': ingr['quantity']}})
                else:
                    for keys, values in result.items():
                        if keys == ingr['ingridient_name']:
                            quantity = values['quantity'] + ingr['quantity']
                            result.update({ingr['ingridient_name']: {'measure': ingr['measure'], 'quantity': quantity}})

    for keys, values in result.items():
        values['quantity'] *= int(person_count)
        print(keys + ': ' + str(values))


dishes = input('Введите блюдо (например вот так: Блюдо) или несколько через запятую (например вот так: Блюдо, Блюдо) - с пробелом после запятой'
               '\n писать регулярку по разбору строки нету времени )))) спасибо за пониманимание: ')

while 1:
    person_count = input('Сколько народа: ')
    if not person_count.isdigit():
        print('Введите количество народа только цифрами')
    else:
        break
get_shop_list_by_dishes(dishes, person_count)


