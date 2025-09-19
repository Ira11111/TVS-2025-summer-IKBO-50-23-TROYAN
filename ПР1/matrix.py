import copy
from typing import List


def print_matrix(matrix: List[List[float]], title="Матрица"):
    """Вывод матрицы на экран"""
    print(f"\n{title}:")
    for row in matrix:
        for element in row:
            print(f"{element: .2f}", end=" ")
        print()
    # print(matrix)


def add(m1: List[List[float]], m2: List[List[float]]):
    res = copy.deepcopy(m1)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] += m2[i][j]
    return res


def sub(m1: List[List[float]], m2: List[List[float]]):
    res = copy.deepcopy(m1)
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res[i][j] -= m2[i][j]
    return res


def scal_mul(m: List[List[float]], a: float):
    res = copy.deepcopy(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            res[i][j] *= a
    return res


def multiply(m1: List[List[float]], m2: List[List[float]]):
    res = [[0 for _ in range(len(m1))] for _ in range(len(m1[0]))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                res[i][j] += m1[i][k] * m2[k][j]
    return res


def transpose(m: List[List[float]]) -> List[List[float]]:
    return [list(row) for row in zip(*m)]


def minor(matrix, i, j):
    """Вычисление минора матрицы (исключение i-й строки и j-го столбца)"""
    return [row[:j] + row[j + 1:] for row_idx, row in enumerate(matrix) if row_idx != i]


def det(matrix):
    """
    Вычисление определителя квадратной матрицы рекурсивным методом
    """
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    d = 0
    for j in range(n):
        # Создаем минор матрицы
        m = minor(matrix, 0, j)
        # Рекурсивно вычисляем определитель минора
        sign = 1 if j % 2 == 0 else -1
        d += sign * matrix[0][j] * det(m)

    return d


def matrix_inverse(matrix):
    """Вычисление обратной матрицы методом Гаусса-Жордана"""
    n = len(matrix)

    # Проверка на квадратность
    if n != len(matrix[0]):
        raise ValueError("Матрица должна быть квадратной")

    # Создаем расширенную матрицу [A|I]
    augmented = []
    for i in range(n):
        row = matrix[i][:]  # Копируем строку исходной матрицы
        # Добавляем единичную матрицу
        row.extend([1 if j == i else 0 for j in range(n)])
        augmented.append(row)

    # Прямой ход метода Гаусса
    for i in range(n):
        # Ищем максимальный элемент в столбце
        max_row = i
        for j in range(i + 1, n):
            if abs(augmented[j][i]) > abs(augmented[max_row][i]):
                max_row = j

        # Меняем строки местами
        augmented[i], augmented[max_row] = augmented[max_row], augmented[i]

        # Проверяем, что диагональный элемент не нулевой
        # if abs(augmented[i][i]) < 1e-10:
        #     raise ValueError("Матрица вырожденная, обратной не существует")

        # Делаем диагональный элемент равным 1
        pivot = augmented[i][i]
        for j in range(2 * n):
            augmented[i][j] /= pivot

        # Обнуляем элементы в столбце
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]

    # Извлекаем обратную матрицу из правой части
    inverse = []
    for i in range(n):
        inverse.append(augmented[i][n:])

    return inverse


def matrix_power(matrix, power):
    res = copy.deepcopy(matrix)
    for i in range(power):
        res = multiply(res, matrix)
    return res
