print('Задание 2')
# Решение предполагает, что координаты, читаемые из файла 1 (circle.txt) и из файла 2 (dot.txt), введены в соответствующей строке (line) через пробел.

import sys
from typing import List, Tuple, Any

def get_data() -> None:
    """
    Функция получает путь к файлам circle.txt и dot.txt из командной строки и вызывает функцию get_coordinates(circle_path, dots_path).
    """
    if len(sys.argv) != 3:
        raise TypeError('Необходмо указать два имени файла через пробел: circle.txt dot.txt')
    circle_path = sys.argv[1]
    dots_path = sys.argv[2]
    get_coordinates(circle_path, dots_path)

def get_coordinates(circle_file: str, dot_file: str) -> None:
    """
    Функция читает файл с координатами центра окружности и её радиусом, а также файл с координатами точки.
    Записывает данные с координатами центра окружности и её радиусом в переменные.
    Формирует список из кортежей с координатами точки.
    Вызывает функцию define_dot_position(x_circle_center, y_circle_center, radius, dots).
    :param circle_file: файл circle.txt, содержащий координаты центра окружности и её радиус.
    :param dot_file: файл dot.txt, содержащий координаты точек в количестве от 1 до 100 включительно.
    Предполагается, что координаты одной точки указываются через пробел на одной строке.
    Координаты каждой другой точки начинаются с новой строки.
    """
    dots = []

    with open(circle_file, 'r') as read_circle_file:
        lines = read_circle_file.readlines()
        coordinate_list = lines[0].split()
        x_circle_center = float(coordinate_list[0])
        y_circle_center = float(coordinate_list[1])
        radius = float(lines[1])
        if not ((10 ** -38) <= x_circle_center <= (10 ** 38)) or not ((10 ** -38) <= y_circle_center <= (10 ** 38))  or not ((10 ** -38) <= radius <= (10 ** 38)):
            raise ValueError('Координаты центра окружности и радиуса должны быть рациональными симслами в диапозоне (10 ** -38) до (10 ** 38) включительно.')

    with open(dot_file, 'r') as read_dot_file:
        lines = read_dot_file.readlines()
        if not (1 <= len(lines) <= 100):
            raise ValueError('Количество точек должно быть от 1 до 100 включительно.')
        for line in lines:
            coordinate_list = line.split()
            x_dot_coord = float(coordinate_list[0])
            y_dot_coord = float(coordinate_list[1])
            dots.append((x_dot_coord, y_dot_coord))

    define_dot_position(x_circle_center, y_circle_center, radius, dots)

def define_dot_position(x_circle_center: float, y_circle_center: float, radius: float, dots: List[Tuple[float]]) -> Any:
    """
    Функция определяет положение каждой точки относительно окружности по следующей легенде:
    - если точка находится внутри окружности, то выводится 1;
    - если точка находится на окружности, то выводится 0;
    - если точка находится снаружи окружности, то выводится 2.
    :param x_circle_center: координата x окружности.
    :param y_circle_center: координата y окружности.
    :param radius: радиус окружности (его длина).
    :param dots: список из кортежей с координатами точек.
    """
    for coordinate_tuple in dots:
        distance_square = (coordinate_tuple[0] - x_circle_center) ** 2 + (coordinate_tuple[1] - y_circle_center) ** 2
        if distance_square < radius ** 2:
            print (1)
        elif distance_square == radius ** 2:
            print (0)
        elif distance_square > radius ** 2:
            print (2)


if __name__ == '__main__':
    get_data()