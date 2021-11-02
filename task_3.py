"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" и обработав исключение,
придумайте как это сделать
"""

WORD_1 = 'attribute'
WORD_2 = 'класс'
WORD_3 = 'функция'
WORD_4 = 'type'
WORD_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]


def el_in_list(some_list):
    try:
        print('\nTry Write elements in bytes:')
        for el in some_list:
            print(bytes(el, 'ascii'))
    except UnicodeEncodeError:
        print(f'Can\'t write "{el}" in bytes')


def main():
    try:
        print('\nProgram "Сan write in bytes or not?"')
        el_in_list(WORD_LIST)
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()