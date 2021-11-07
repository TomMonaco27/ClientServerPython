"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "принтер",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json

DICT_ORDER_TO_JSON = {
    "item": "computer1",
    "quantity": "200",
    "price": "100000",
    "buyer": "No name",
    "date": "01.12.2021"
    }
NAME_FILE_JSON = "orders.json"


def write_order_to_json(item, quantity, price, buyer, date):
    try:
        with open(NAME_FILE_JSON, 'r', encoding='utf-8') as f_load_json:
            data = json.load(f_load_json)

        with open(NAME_FILE_JSON, 'w', encoding='utf-8') as f_write_json:
            orders_list = data['orders']
            order_el_add = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
            orders_list.append(order_el_add)
            json.dump(data, f_write_json, indent=4, ensure_ascii=False)
    except:
        print('Error write_order_to_json()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def write_order_to_json2(dict_order_to_JSON):
    try:
        with open(NAME_FILE_JSON, 'r', encoding='utf-8') as f_load_json:
            data = json.load(f_load_json)

        with open(NAME_FILE_JSON, 'w', encoding='utf-8') as f_write_json:
            orders_list = data['orders']
            orders_list.append(dict_order_to_JSON)
            json.dump(data, f_write_json, indent=4, ensure_ascii=False)
    except:
        print('Error write_order_to_json2()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')



def main():
    try:
        print('\nProgram "Work with json file"')
        write_order_to_json("computer", "20", "50000", "Sidorov", "07.11.2011")
        write_order_to_json2(DICT_ORDER_TO_JSON)
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()