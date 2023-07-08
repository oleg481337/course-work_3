import json
from classes import Operation


def get_json_to_list(adress):
    """
    Получить список операций из файла operation.json
    :return:
    """
    with open(adress, 'r', encoding="UTF-8") as file:
        list_operation = json.load(file)
    return list_operation


def create_ex_class():
    """
    Создать список экземпляров класса
    :return:
    """
    list_ex_class = []
    list_from_json = get_json_to_list('operations.json')
    list_from_json.sort(key=lambda d: d['date'], reverse=True)
    for i in list_from_json:
        if 'from' in i.keys():
            list_ex_class.append(Operation(i['date'],
                                           i['description'],
                                           i['to'],
                                           i['operationAmount']['currency']['name'],
                                           i['operationAmount']['amount'],
                                           i['state'],
                                           i['from']))

        else:
            list_ex_class.append(Operation(i['date'],
                                           i['description'],
                                           i['to'],
                                           i['operationAmount']['currency']['name'],
                                           i['operationAmount']['amount'],
                                           i['state']))
    return list_ex_class


def beautiful_result(operation):
    """Вывод результата в требуемом формате"""
    if operation.from_ is None:
        print(operation.beautiful_data(), operation.description)
        print(operation.to)
        print(operation.summa, operation.currency)
        print()
        return True
    else:
        print(operation.beautiful_data(), operation.description)
        print(f'{operation.from_}  ->  {operation.to}')
        print(operation.summa, operation.currency)
        print()
        return True
