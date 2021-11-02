"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

WORD_1 = 'разработка'
WORD_2 = 'администрирование'
WORD_3 = 'protocol'
WORD_4 = 'standard'
WORD_LIST = [WORD_1, WORD_2, WORD_3, WORD_4]
str_to_byte_list = []
byte_to_str_list = []


def str_to_byte(words_list):
    for el in words_list:
        el_bytes = el.encode('utf-8')
        str_to_byte_list.append(el_bytes)
    print(f'Список строк в utf-8: {str_to_byte_list}')


def byte_to_str(byte_list):
    for el_bytes in byte_list:
        el_str = el_bytes.decode('utf-8')
        byte_to_str_list.append(el_str)
    print(f'Список расшифрованных строк: {byte_to_str_list}')


def main():
    try:
        print('\nProgram "Str to Byte and vice versa"')
        str_to_byte(WORD_LIST)
        byte_to_str(str_to_byte_list)
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()