"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

NAME_SITE = ['ping', 'yandex.ru']


def ping_sites(NAME_SITE):
    STR_PING = subprocess.Popen(NAME_SITE, stdout=subprocess.PIPE)
    for line in STR_PING.stdout:
        result_string = chardet.detect(line)
        print(f'ping: {result_string}')
        line = line.decode(result_string['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


def main():
    try:
        print('\nProgram "Ping web-sites "')
        ping_sites(NAME_SITE)
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
                  ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()