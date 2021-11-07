"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml


DATA_DICT_TO_YAML = {'object': ['ball', 'plane', 'pen'],
                    'quantity': 3,
                    'price': {'ball': '100\u20ac',
                                    'plane': '20000000\u20ac',
                                    'pen': '5\u20ac'}
           }
FILE_NAME_YAML = "file.yaml"


def write_to_yaml(file_name_yaml):
    try:
        with open(file_name_yaml, 'w', encoding='utf-8') as f_in:
            yaml.dump(DATA_DICT_TO_YAML, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)
    except:
        print('Error write_to_yaml()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def read_from_yaml(file_name_yaml):
    try:
        with open(file_name_yaml, 'r', encoding='utf-8') as f_out:
            data_dict_from_yaml = yaml.load(f_out, Loader=yaml.SafeLoader)
    except:
        print('Error read_from_yaml()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    return data_dict_from_yaml


def compare_data_yaml():
    return (print("DATA is Equal") if DATA_DICT_TO_YAML == read_from_yaml(FILE_NAME_YAML) else print("DATA is NOT Equal"))


def main():
    try:
        print('\nProgram "Work with yaml file"')
        write_to_yaml(FILE_NAME_YAML)
        compare_data_yaml()
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()