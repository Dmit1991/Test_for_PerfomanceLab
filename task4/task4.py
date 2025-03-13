print('Задание 4')

import sys
from typing import List

def count_min_actions(numbers: List[int]):
    """
    Функция выводит результат вычислений минимального количества действий, требуемых для приведения всех элементов к одному числу.
    :param numbers: список чисел, сформированный в основной функции программы по результатам чтения файла, содержащего числа.
    """
    amount_actions = 0
    numbers.sort()
    mediana = numbers[len(numbers) // 2]

    for number in numbers:
        amount_actions += abs(number - mediana)
    print (amount_actions)

def main():
    """
    Функция является основвной.
    Читает файл, содержащий числа, и формирует список numbers для передачи его в качестве аргумента функции count_min_actions(numbers)
    """
    if len(sys.argv) != 2:
        raise TypeError('Необходмо указать одно имя файла: numbers.txt')
    numbers_file = sys.argv[1]

    with open(numbers_file, 'r') as read_numbers_file:
        lines = read_numbers_file.readlines()
        numbers = [int(n) for n in lines]

    count_min_actions(numbers)


if __name__ == '__main__':
    main()