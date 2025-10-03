import pytest
import math
from figure.circle import Circle


class TestCircleValidation:
    """Тесты валидации круга"""

    def test_valid_circle_creation(self):
        """Тест создания валидного круга"""
        circle = Circle(5.0)
        assert circle.radius == 5.0

        circle2 = Circle(1)
        assert circle2.radius == 1

    def test_negative_radius_raises_error(self):
        """Тест отрицательного радиуса"""
        with pytest.raises(ValueError, match="radius must be greater than 0"):
            Circle(-1)
        with pytest.raises(ValueError, match="radius must be greater than 0"):
            Circle(-5.0)

    def test_zero_radius_raises_error(self):
        """Тест нулевого радиуса"""
        with pytest.raises(ValueError, match="radius must be greater than 0"):
            Circle(0)


class TestCircleMethods:
    """Тесты методов круга"""

    def test_area_calculation(self):
        """Тест вычисления площади"""
        circle = Circle(1.0)
        expected_area = math.pi * 1.0  # π * r²
        assert circle.area() == pytest.approx(expected_area, abs=1e-10)

        circle2 = Circle(2.0)
        expected_area2 = math.pi * 4.0  # π * 2²
        assert circle2.area() == pytest.approx(expected_area2, abs=1e-10)

    def test_perimeter_calculation(self):
        """Тест вычисления периметра"""
        circle = Circle(1.0)
        expected_perimeter = 2 * math.pi * 1.0  # 2πr
        assert circle.perimeter() == pytest.approx(expected_perimeter, abs=1e-10)

        circle2 = Circle(2.5)
        expected_perimeter2 = 2 * math.pi * 2.5
        assert circle2.perimeter() == pytest.approx(expected_perimeter2, abs=1e-10)

    def test_diameter_calculation(self):
        """Тест вычисления диаметра"""
        circle = Circle(3.0)
        assert circle.diameter() == 6.0

        circle2 = Circle(1.5)
        assert circle2.diameter() == 3.0

    def test_area_perimeter_relationship(self):
        """Тест соотношения площади и периметра"""
        circle = Circle(2.0)
        area = circle.area()
        perimeter = circle.perimeter()

        # P = 2πr, A = πr² => A = (P²)/(4π)
        calculated_area_from_perimeter = (perimeter ** 2) / (4 * math.pi)
        assert area == pytest.approx(calculated_area_from_perimeter, abs=1e-10)


class TestCircleProperties:
    """Тесты свойств круга"""

    def test_mathematical_relationships(self):
        """Тест математических соотношений"""
        circle = Circle(3.0)

        # Площадь = π * r²
        assert circle.area() == pytest.approx(math.pi * 9, abs=1e-10)

        # Периметр = 2 * π * r
        assert circle.perimeter() == pytest.approx(2 * math.pi * 3, abs=1e-10)

        # Диаметр = 2 * r
        assert circle.diameter() == 6.0

    def test_consistency_across_operations(self):
        """Тест согласованности операций"""
        circle = Circle(4.0)

        # Площадь через разные вычисления
        area_from_radius = math.pi * 16
        area_from_method = circle.area()
        assert area_from_method == pytest.approx(area_from_radius, abs=1e-10)

        # Периметр через диаметр
        perimeter_from_diameter = math.pi * circle.diameter()
        perimeter_from_method = circle.perimeter()
        assert perimeter_from_method == pytest.approx(perimeter_from_diameter, abs=1e-10)


class TestCircleEdgeCases:
    """Тесты граничных случаев"""

    def test_small_radius(self):
        """Тест маленького радиуса"""
        circle = Circle(0.001)
        area = circle.area()
        perimeter = circle.perimeter()

        assert area > 0
        assert perimeter > 0
        assert circle.diameter() == 0.002

    def test_very_small_radius(self):
        circle = Circle(1e-10)
        assert circle.area() > 0

    def test_large_radius(self):
        """Тест большого радиуса"""
        circle = Circle(1000.0)
        area = circle.area()
        perimeter = circle.perimeter()

        expected_area = math.pi * 1000000
        expected_perimeter = 2 * math.pi * 1000

        assert area == pytest.approx(expected_area, abs=1e-6)
        assert perimeter == pytest.approx(expected_perimeter, abs=1e-6)

    def test_floating_point_radius(self):
        """Тест радиуса как float"""
        circle = Circle(2.5)
        area = circle.area()
        perimeter = circle.perimeter()

        expected_area = math.pi * 6.25
        expected_perimeter = 2 * math.pi * 2.5

        assert area == pytest.approx(expected_area, abs=1e-10)
        assert perimeter == pytest.approx(expected_perimeter, abs=1e-10)

    def test_unit_circle_properties(self):
        """Тест свойств единичного круга"""
        circle = Circle(1.0)
        assert circle.area() == pytest.approx(math.pi, abs=1e-10)
        assert circle.perimeter() == pytest.approx(2 * math.pi, abs=1e-10)
        assert circle.diameter() == 2.0


    def test_extreme_precision_cases(self):
        """Тесты для крайних случаев точности"""
        # Тест на очень маленькие значения
        circle = Circle(1e-8)
        assert circle.diameter() == 2e-8
        assert circle.area() > 0

        # Тест на очень большие значения
        circle = Circle(1e8)
        assert circle.diameter() == 2e8
        assert circle.area() < float('inf')


class TestCirclePrecision:
    """Тесты точности вычислений"""

    def test_area_precision(self):
        """Тест точности вычисления площади"""
        circle = Circle(1.0)
        area = circle.area()
        expected = math.pi
        assert abs(area - expected) < 1e-10

    def test_perimeter_precision(self):
        """Тест точности вычисления периметра"""
        circle = Circle(1.0)
        perimeter = circle.perimeter()
        expected = 2 * math.pi
        assert abs(perimeter - expected) < 1e-10

    def test_diameter_precision(self):
        """Тест точности вычисления диаметра"""
        circle = Circle(1.0)
        diameter = circle.diameter()
        assert diameter == 2.0