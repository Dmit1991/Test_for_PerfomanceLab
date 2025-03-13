print('Задание 3')

import json
import sys
from typing import List, Dict, Any

def write_values(tests: List[Dict[str, Any]], values: Dict[int, str]) -> None:
    """
    Функция записывает (обновляет) значения поля 'value' в десериализованных данных из тестов, рекурсивно обходя вложенность.
    :param tests: полученный в результате десериализации данных из файла с тестами и последующего рекурсивного обхода список тестов,
    каждый из которых является словарём.
    :param values: сформированный в результате десериализации данных из файла с результатами теста (values) словарь,
    в котором ключами являются идентификаторы тестов, а значениями - их результаты.
    :return: None
    """
    for test in tests:
        if test['id'] in values:
            test['value'] = values[test['id']]
        if 'values' in test:
            write_values(test['values'], values)

def main():
    """
    Функция является основной.
    Обрабатывает три аргумента командной строки с указанием имени файлов.
    Читает файлы формата JSON с тестами и их результатами, проводит их десериализацию для получения данных из них.
    Выполняет действия с десериализованными данными, передавая их аргументами вызываемой функции write_values (tests, values).
    Записывает данные с результатами тестов в файл report, сериализуя их в JSON-формат.
    """
    if len(sys.argv) != 4:
        raise TypeError('Необходмо указать три имени файла через пробел: tests.json values.json report.json')
    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    with open (tests_file, 'r') as read_tests_file:
        tests_data = json.load(read_tests_file)

    with open(values_file, 'r') as read_values_file:
        values_data = json.load(read_values_file)

    values_dict = {item['id']: item['value'] for item in values_data['values']}
    write_values(tests_data['tests'], values_dict)

    with open(report_file, 'w') as written_report_file:
        json.dump(tests_data, written_report_file, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
