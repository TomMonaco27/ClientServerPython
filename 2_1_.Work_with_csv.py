"""
Задание на закрепление знаний по модулю CSV.
 Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и
 формирующий новый «отчетный» файл в формате CSV. Для этого:

 Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
 их открытие и считывание данных.
 В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
 «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
 начения каждого параметра поместить в соответствующий список.
 Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
 В этой же функции создать главный список для хранения данных отчета — например,
 main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
 «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
 Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
 В этой функции реализовать получение данных через вызов функции get_data(),
 а также сохранение подготовленных данных в соответствующий CSV-файл;
 Проверить работу программы через вызов функции write_to_csv().
"""

import csv
import re

main_data = [["Изготовитель системы","Название ОС","Код продукта","Тип системы"]]
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []
NOT_FOUND = "Not found"
PREFIX_NAME_TEXT_FILE = "info_"
NUMBER_TEXT_FILES = 3
NUMBER_INFO_COLUMNS = 4
read_string = []
match_os_code = ""
name_csv_file_to_save_data = "data_report.csv"
temp_os_prod_list = []
temp_os_name_list = []
temp_os_code_list = []
temp_os_type_list = []
temp_list = []
temp_el = ""
#i = 1


#def get_data ():
#    with open('info_1.txt') as f_n:
#        F_N_READER = csv.reader(f_n)
#        print(type(F_N_READER))
#        for row in F_N_READER:
#            print(row)


def open_text_file(PREFIX_NAME_TEXT_FILE, NUMBER_TEXT_FILES):
    #i = 1
    try:
        for i in range(1, NUMBER_TEXT_FILES+1):
            #i = i + 1
            name_text_file = PREFIX_NAME_TEXT_FILE + str(i) + ".txt"
            with open(name_text_file, 'r', encoding="UTF-8") as f_obj:
                print(f'1. Opening file: {name_text_file}')
                for line in f_obj:
                    match_os_prod = re.search(r'Изготовитель системы:', line)
                    if match_os_prod:
                        temp_line = line.split(":")
                        match_os_prod = "".join(c for c in temp_line[1] if c.isalpha())
                        os_prod_list.append(match_os_prod)
                        #temp_list.append(os_prod_list)
                        #print(temp_list)

                        #os_prod_list = line.split(':')
                    #print(match_os_prod.split)
                    #result = re.split(r' ', match_os_prod[0])
                    match_os_name = re.search(r'Windows\s\d..', line)
                    match_os_code = re.search(r'\d{5}-\w{3}-\d{7}-\d{5}', line)

                    match_os_type = re.search(r'Тип системы:', line)
                    if match_os_type:
                        temp_line = line.split(":")
                        match_os_type = "".join(c for c in temp_line[1] if c.isalnum())
                        os_type_list.append(match_os_type)
                        #temp_list.append(",".join(os_type_list))
                        #os_type_list.append(line.split(':'))
                        #os_type_list = line.split(':')

                    #os_prod_list.append(match_os_prod[0]) if match_os_prod else ''
                    os_name_list.append(match_os_name[0]) if match_os_name else ''
                    os_code_list.append(match_os_code[0]) if match_os_code else ''


                    #temp_list.append("".join(os_name_list))
                    #temp_list.append(",".join(os_code_list))
                    #os_type_list.append(match_os_type[0]) if match_os_type else ''

                    #print(os_prod_list.append(match_os_prod[0]) if match_os_prod else '')
                    #print(os_name_list.append(match_os_name[0]) if match_os_name else '')
                    #print(os_code_list.append(match_os_code[0]) if match_os_code else '')
                #main_data.append(os_prod_list)
                print(f'2. Close file: {name_text_file}\n')
                #temp_list.append(os_prod_list)
                #print(temp_list)
                #print(result)
                #print(match_os_prod)
        #os_prod_list.append(i)
        #for i in range(4):
        #    main_data.append(os_prod_list[i])
        #main_data.append(os_prod_list)
        #main_data.append(os_name_list)
        #main_data.append(os_code_list)
        #main_data.append(os_type_list)
        sort_main_data(os_prod_list, os_name_list, os_code_list, os_type_list, NUMBER_TEXT_FILES, NUMBER_INFO_COLUMNS)
        #print(main_data)
        print("os_prod_list = ", os_prod_list)
        print("os_name_list = ", os_name_list)
        print("os_code_list = ",os_code_list)
        print("os_type_list = ", os_type_list)

                    #print(match_os_code.group(0))
#                    if match_os_code[0]:
#                        os_code_list.append(match_os_code)
#                        print(os_code_list)
                    #print(type(line))
                    #print(line.strip())

                #read_string = f_obj.readlines()
                #print(read_string)
                #for num, el in enumerate(read_string_list):
                #    words_in_string = len(el.split())
                #    print(f'Words in string {num} is {words_in_string}')

    except IOError:
        print('Error open_text_file(). Input-output error!')
    except:
        print('Error open_text_file()! Something wrong, but don\'t worry, be happy.' 
              ' Maybe next time, buy yourself a ice cream :)')
    #return main_data

def sort_main_data(os_prod_list,os_name_list,os_code_list, os_type_list, NUMBER_TEXT_FILES, NUMBER_INFO_COLUMNS):
    #for i in range(temp_list):
    #    temp_list.append(os_prod_list[i])
    #    temp_list.append(os_name_list[i])
    #    temp_list.append(os_code_list[i])
    #    temp_list.append(os_type_list[i])
    #     print(temp_list)
    #for row in os_prod_list:
    #    temp_os_prod_list.append(row)
    #print("temp_list = ", temp_os_prod_list)
    #temp_list.append(temp_os_prod_list)

    #for row in os_name_list:
    #    temp_os_name_list.append(row)
    #print("temp_list = ", temp_os_name_list)

    #for row in os_code_list:
    #    temp_os_code_list.append(row)
    #print("temp_list = ", temp_os_code_list)

    #for row in os_type_list:
    #    temp_os_type_list.append(row)
    #print("temp_list = ", temp_os_type_list)

    for i in range(NUMBER_INFO_COLUMNS):
        temp_el = os_prod_list[i]
        temp_os_prod_list.append(temp_el)

        main_data.append()
        print(os_prod_list[i], temp_el, type(os_prod_list[i]), type(temp_el))
        #temp_list
    #    temp_os_prod_list.append(i)

        #temp_list.append(temp_os_prod_list[i] + ","  + temp_os_name_list[i] + "," + temp_os_code_list[i] + "," + temp_os_type_list[i])
        #print("temp_list_FINAL = ", temp_list)



        #column = [];  # пустой список

            #temp_list.insert(i, os_prod_list[i])
        #temp_list.insert(0, os_name_list[i])
        #temp_list.insert(0, os_code_list[i])
        #temp_list.insert(0, os_type_list[i])
        main_data.append(temp_list)
        #main_data[i] = os_prod_list[i]


        #for j in range(i):
            #main_data.append(j)
        #main_data.append(os_prod_list[i])
        #main_data.append(os_name_list[i])
        #main_data.append(os_code_list[i])
        #main_data.append(os_type_list[i])
        #temp_list.clear()
        #temp_list.append(os_prod_list[i])
        #temp_list.append(os_name_list[i])
        #temp_list.append(os_code_list[i])
        #temp_list.append(os_type_list[i])

        #main_data.insert(i+1, temp_list[i])
        #temp_list.clear()

        #main_data[i]
        #print("temp list = ", temp_list)
        #main_data.append(temp_list)
        #main_data.append(os_prod_list[i])
        #main_data = main_data + temp_list
    print("main_data = ",main_data)
    print("temp_list = ", temp_list)


def write_to_csv(name_csv_file_to_save_data):
    with open(name_csv_file_to_save_data, 'w', encoding="utf-8") as f_n:
        F_N_WRITER = csv.writer(f_n)
        #for i, val in enumerate(seq, start=1):
        #for i in main_data:
        #    for j in i:
        #        F_N_WRITER.write(j)
        #        print(j)
        for row in main_data:
            F_N_WRITER.writerow(row)

#with open('kp_data_write_1.csv') as f_n:
#    print(type(f_n.read()))


def main():
    try:
        print('\nProgram "Read some info from txt file and write to csv"')
        open_text_file(PREFIX_NAME_TEXT_FILE, NUMBER_TEXT_FILES)
        write_to_csv(name_csv_file_to_save_data)
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()