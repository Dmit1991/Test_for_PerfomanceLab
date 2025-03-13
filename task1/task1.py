print('Задание 1')

import sys
from typing import Any

def get_data() -> None:
    """
    Функция получает аргументы n и m из командной строки и вызывает функцию get_path(n, m).
    """
    if len(sys.argv) != 3:
        raise TypeError('Необходмо указать два аргумента через пробел: n m')
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    get_path(n, m)

def get_path(n: int, m: int) -> Any:
    """
    Функция принимает аргументами своих параметров целые числа n и m.
    С 1 и по число n (включительно) формируется список чисел numbers в строковом представлении.
    Целое число m: интервал длины для передвижения по списку numbers, влияющий на индекс его элементов.
    Функция возвращает строку с подстрокой path, состоящей из начальных элементов полученных интервалов.
    """
    numbers = [str(n) for n in range(1, n + 1)]
    index = 0
    path = ''

    while True:
        path += numbers[index]
        index = (index + m - 1) % n
        if index == 0:
            break
    print(f'Полученный путь: {path}')

if __name__ == '__main__':
    get_data()



