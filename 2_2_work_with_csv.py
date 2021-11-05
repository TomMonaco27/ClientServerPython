import os
import re
import csv

FILE_NAME = "data_report2"


def get_data():
    try:
        file_pattern = '^info.*\.txt$'
        main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

        for file in os.listdir('.'):

            if os.path.isfile(file) and re.match(file_pattern, file):
                print(file)
                print(parse_data(file))
                main_data.append(parse_data(file))

        return main_data
    except IOError:
        print('Error get_data(). Input-output error!')
    except:
        print('Error get_data()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def parse_data(file):
    #os_manufacturer_pattern = '^Изготовитель ОС:\s*(.)$'
    os_name_pattern = '^Название ОС:\s(.)$'
    os_product_code_pattern = '^Код продукта:\s(.)$'
    os_type_pattern = '^Тип системы:\s(.*)$'
    result = []

    os_manufacturer_pattern = '^Изготовитель ОС:\s'

    with open(file, 'r', encoding="utf-8") as find_file:
        for line in find_file:
            #print(line)
            matched_os_manufacturer = re.match(os_manufacturer_pattern, line)
            #print(matched_os_manufacturer)
            matched_os_name = re.match(os_name_pattern, line)
            matched_os_product_code = re.match(os_product_code_pattern, line)
            matched_os_type = re.match(os_type_pattern, line)

            #matched_os_manufacturer = re.search(r'Windows\s\d..', line)

        if matched_os_manufacturer:
            if matched_os_manufacturer:
                print('1')
                result.append(matched_os_manufacturer[1])
            else:
                print('2')
                result.append('None')

        if matched_os_name:
            if matched_os_name:
                result.append(matched_os_name[1])
            else:
                result.append('None')

        if matched_os_product_code:
            if matched_os_product_code:
                result.append(matched_os_product_code[1])
            else:
                result.append('None')

        if matched_os_type:
            if matched_os_type:
                result.append(matched_os_type[1])
            else:
                result.append('None')
    return result


def write_to_csv(csv_file):
    try:
        if not re.match('.*.csv$', csv_file):
            csv_file += '.csv'

        with open(csv_file, 'w', encoding="utf-8", newline='') as res_file:
            writer = csv.writer(res_file)
            for row in get_data():
                writer.writerow(row)

        print(f"Created file: {csv_file}")
    except IOError:
        print('Error write_to_csv(). Input-output error!')
    except:
        print('Error write_to_csv()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')


def main():
    try:
        print('\nProgram "Read some info from txt file and write to csv"')
        write_to_csv(FILE_NAME)
    except:
        print('Error main()! Something wrong, but don\'t worry, be happy.'
              ' Maybe next time, buy yourself a ice cream :)')
    finally:
        print('\nSee you soon. End the program.')


if __name__ == '__main__':
    main()
