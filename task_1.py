"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции

ВНИМАНИЕ!!: сдача задания
1) создать папку Lesson_1_Ivanov
2) в папку положить файлы task_1 - task_6 (а также txt-файл для последнего)
3) заархивировать папку! и сдать архив

Все другие варианты сдачи приму только один раз, потом буду ставить НЕ СДАНО
"""

# представить в буквенном формате
WORD_1 = 'разработка'
WORD_2 = 'сокет'
WORD_3 = 'декоратор'

# с помощью онлайн-конвертера преобразовать в набор кодовых точек Unicode
# используя веб-сайт: https://www.branah.com/unicode-converter
WORD_1_UNICODE = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
WORD_2_UNICODE = '\u0441\u043e\u043a\u0435\u0442'
WORD_3_UNICODE = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

WORDS_LIST = [WORD_1, WORD_2, WORD_3]
WORD_UNICODE_LIST = [WORD_1_UNICODE, WORD_2_UNICODE, WORD_3_UNICODE]


# проверить тип и содержание соответствующих переменных
def el_and_types_in_list(some_list):
    print('\nType and elements in list:')
    for el in some_list:
        print(f'Элемент: {el}')
        print(f'Тим строки: {type(el)}\n')



# проверить тип и содержание соответствующих переменных в формате
def el_and_types_in_unicode_list(some_unicode_list):
    print('\nType and elements in UNICODE list:')
    for el in some_unicode_list:
        print(f'Элемент: {el}')
        print(f'Тим строки: {type(el)}\n')

def main():
    try:
        print('\nProgram "Work with unicode"')
        el_and_types_in_list(WORDS_LIST)
        el_and_types_in_unicode_list(WORD_UNICODE_LIST)

    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()