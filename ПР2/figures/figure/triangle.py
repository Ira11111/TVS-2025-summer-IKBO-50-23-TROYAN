import math
from figure import Figure


class Triangle(Figure):
    def __init__(self, s1: float, s2: float, s3: float) -> None:
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self._validate_sides()

    def _validate_sides(self):
        """Валидация сторон треугольника с раздельными проверками."""
        # Проверка положительности каждой стороны отдельно
        side1_valid = self.side1 > 0
        side2_valid = self.side2 > 0
        side3_valid = self.side3 > 0

        if not side1_valid:
            raise ValueError("Invalid triangle sides")
        if not side2_valid:
            raise ValueError("Invalid triangle sides")
        if not side3_valid:
            raise ValueError("Invalid triangle sides")

        # Проверка неравенства треугольника
        sides = self.get_sides()
        a, b, c = sorted(sides)

        sum_shorter = a + b
        is_triangle_valid = sum_shorter > c

        if not is_triangle_valid:
            raise ValueError("Invalid triangle sides")

    def get_sides(self):
        """Возвращает кортеж сторон."""
        return (self.side1, self.side2, self.side3)

    def area(self):
        """Вычисление площади по формуле Герона."""
        # Вычисление полупериметра
        p = self.perimeter()
        semi_perimeter = p / 2.0

        # Разности для формулы Герона
        diff1 = semi_perimeter - self.side1
        diff2 = semi_perimeter - self.side2
        diff3 = semi_perimeter - self.side3

        # Проверка возможности вычисления
        can_compute_area = diff1 > 0 and diff2 > 0 and diff3 > 0

        if not can_compute_area:
            return 0.0

        # Вычисление произведения
        product1 = semi_perimeter * diff1
        product2 = product1 * diff2
        product = product2 * diff3

        # Проверка на отрицательное значение
        if product <= 0:
            return 0.0

        area_value = math.sqrt(product)
        return area_value

    def perimeter(self):
        """Вычисление периметра."""
        sum1 = self.side1 + self.side2
        perimeter_value = sum1 + self.side3
        return perimeter_value

    def is_right(self):
        """Проверка, является ли треугольник прямоугольным."""
        # Сортируем стороны
        sides = self.get_sides()
        a, b, c = sorted(sides)

        # Вычисляем квадраты
        a_sq = a * a
        b_sq = b * b
        c_sq = c * c

        # Проверяем теорему Пифагора
        sum_of_squares = a_sq + b_sq
        difference = abs(sum_of_squares - c_sq)

        tolerance = 1e-7
        is_right_angled = difference < tolerance

        return is_right_angled

    def is_equilateral(self) -> bool:
        """Проверка, является ли треугольник равносторонним."""
        a, b, c = self.get_sides()

        sides_equal_ab = abs(a - b) < 1e-10
        sides_equal_bc = abs(b - c) < 1e-10

        return sides_equal_ab and sides_equal_bc

    def is_isosceles(self) -> bool:
        """Проверка, является ли треугольник равнобедренным."""
        a, b, c = self.get_sides()

        # Проверяем все возможные пары равных сторон
        ab_equal = abs(a - b) < 1e-10
        bc_equal = abs(b - c) < 1e-10
        ac_equal = abs(a - c) < 1e-10

        return ab_equal or bc_equal or ac_equal
