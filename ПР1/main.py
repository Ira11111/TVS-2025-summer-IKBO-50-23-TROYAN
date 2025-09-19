import matrix as m


def input_matrix():
    """Ввод матрицы с клавиатуры"""
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))

        print(f"Введите элементы матрицы {rows}x{cols} построчно (через пробел):")
        matrix = []

        for i in range(rows):
            try:
                row = list(map(float, input(f"Строка {i + 1}: ").split()))
                # if len(row) != cols:
                #     print(f"Ошибка: должно быть {cols} элементов в строке")
                #     raise ValueError
                matrix.append(row)
            except ValueError:
                return None
        return matrix

    except ValueError:
        print("Ошибка: введите целые числа для размерности")
        return None


def matrix_addition():
    """Сложение матриц"""
    print("Введите первую матрицу:")
    m1 = input_matrix()
    if m1 is None: return

    print("Введите вторую матрицу:")
    m2 = input_matrix()
    if m2 is None: return

    # if len(m1) != len(m2) or (len(m1[0]) != len(m2[0])):
    #     print("Ошибка: матрицы должны быть одинаковой размерности")
    #     return
    result = m.add(m1, m2)

    m.print_matrix(result, "Результат сложения")


def matrix_subtraction():
    """Вычитание матриц"""
    print("Введите первую матрицу:")
    m1 = input_matrix()
    if m1 is None: return

    print("Введите вторую матрицу:")
    m2 = input_matrix()
    if m2 is None: return

    if len(m1) != len(m2) or (len(m1[0]) != len(m2[0])):
        print("Ошибка: матрицы должны быть одинаковой размерности")
        return

    result = m.sub(m1, m2)
    m.print_matrix(result, "Результат вычитания")


def matrix_scalar_multiplication():
    """Умножение матрицы на число"""
    print("Введите матрицу:")
    matrix = input_matrix()
    if matrix is None: return

    try:
        scalar = float(input("Введите число для умножения: "))
    except ValueError:
        print("Ошибка: введите число")
        return

    result = m.scal_mul(matrix, scalar)
    m.print_matrix(result, "Результат умножения на число")


def matrix_multiplication():
    """Умножение матриц"""
    print("Введите первую матрицу:")
    m1 = input_matrix()
    if m1 is None: return

    print("Введите вторую матрицу:")
    m2 = input_matrix()
    if m2 is None: return

    # if len(m1[0]) != len(m2):
    #     print("Ошибка: число столбцов первой матрицы должно равняться числу строк второй")
    #     return

    result = m.multiply(m1, m2)
    m.print_matrix(result, "Результат умножения матриц")


def matrix_transpose():
    """Транспонирование матрицы"""
    print("Введите матрицу:")
    matrix = input_matrix()
    if matrix is None: return

    result = m.transpose(matrix)
    m.print_matrix(result, "Транспонированная матрица")


def matrix_determinant():
    """Вычисление определителя"""
    print("Введите квадратную матрицу:")
    matrix = input_matrix()
    if matrix is None: return

    if len(matrix) != len(matrix[0]):
        print("Ошибка: матрица должна быть квадратной")
        return

    try:
        d = m.det(matrix)
        print(f"\nОпределитель матрицы: {d:.2f}")
    except:
        print("Ошибка при вычислении определителя")


def matrix_inverse():
    """Вычисление обратной матрицы"""
    print("Введите квадратную матрицу:")
    matrix = input_matrix()
    if matrix is None: return

    if len(matrix) != len(matrix[0]):
        print("Ошибка: матрица должна быть квадратной")
        return

    # d = m.det(matrix)
    # if abs(d) < 1e-10:
    #     print("Ошибка: определитель равен нулю, обратной матрицы не существует")
    #     return

    res = m.matrix_inverse(matrix)
    m.print_matrix(res, "Обратная матрица")

def matrix_power():
    """Возведение матрицы в степень"""
    print("Введите квадратную матрицу:")
    matrix = input_matrix()
    if matrix is None: return

    if len(matrix) != len(matrix[0]):
        print("Ошибка: матрица должна быть квадратной")
        return

    try:
        power = int(input("Введите степень (натуральное число): "))
        # if power < 1:
        #     print("Ошибка: степень должна быть натуральным числом больше 1")
        #     return

        result = m.matrix_power(matrix, power)
        m.print_matrix(result, f"Матрица в степени {power}")
    except ValueError:
        print("Ошибка: введите целое число для степени")
    except:
        print("Ошибка при возведении в степень")


def main():
    """Главное меню программы"""
    while True:
        print("\n" + "=" * 50)
        print("Калькулятор матриц")
        print("=" * 50)
        print("1. Ввод матрицы")
        print("2. Сложение матриц")
        print("3. Вычитание матриц")
        print("4. Умножение матрицы на число")
        print("5. Умножение матриц")
        print("6. Транспонирование матрицы")
        print("7. Вычисление определителя")
        print("8. Вычисление обратной матрицы")
        print("9. Возведение матрицы в степень")
        print("0. Выход")
        print("=" * 50)

        choice = input("Выберите операцию (0-9): ")

        if choice == '0':
            print("Выход из программы...")
            break
        elif choice == '1':
            matrix = input_matrix()
            if matrix is not None:
                m.print_matrix(matrix)
        elif choice == '2':
            matrix_addition()
        elif choice == '3':
            matrix_subtraction()
        elif choice == '4':
            matrix_scalar_multiplication()
        elif choice == '5':
            matrix_multiplication()
        elif choice == '6':
            matrix_transpose()
        elif choice == '7':
            matrix_determinant()
        elif choice == '8':
            matrix_inverse()
        elif choice == '9':
            matrix_power()
        elif choice == '228':
            print("Otsosylka")
        # else:
        #     print("Неверный выбор. Попробуйте снова.")

        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()
