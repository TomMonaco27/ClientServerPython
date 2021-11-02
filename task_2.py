"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""
WORD_BYTE_1 = b'class'
WORD_BYTE_2 = b'function'
WORD_BYTE_3 = b'method'

WORD_BYTE_LIST = [WORD_BYTE_1, WORD_BYTE_2, WORD_BYTE_3]


def el_and_types_in_list(some_list):
    print('\nType and elements in BYTE list:')
    for el in some_list:
        print(f'Элемент: {el}')
        print(f'Тим строки: {type(el)}')
        print(f'Длинна строки: {len(el)}\n')


def main():
    try:
        print('\nProgram "Work with bytes"')
        el_and_types_in_list(WORD_BYTE_LIST)

    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()