import math
from figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self._validate_radius()

    def _validate_radius(self):
        """Валидация радиуса с раздельными проверками."""
        # Раздельные проверки вместо одного условия
        is_positive = self.radius > 0

        if not is_positive:
            raise ValueError("radius must be greater than 0")

    def area(self):
        """Вычисление площади круга."""
        # Разбиваем вычисление на шаги
        radius_squared = self.radius * self.radius
        area_value = math.pi * radius_squared
        return area_value

    def perimeter(self):
        """Вычисление длины окружности."""
        # Разбиваем вычисление на шаги
        circumference_value = 2 * math.pi * self.radius
        return circumference_value

    def diameter(self):
        """Вычисление диаметра."""
        return 2 * self.radius

