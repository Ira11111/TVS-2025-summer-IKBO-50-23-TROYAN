import pytest
import math
from figure.triangle import Triangle


class TestTriangleValidation:
    """Тесты валидации треугольника"""

    def test_valid_triangle_creation(self):
        """Тест создания валидного треугольника"""
        triangle = Triangle(3, 4, 5)
        assert triangle.side1 == 3
        assert triangle.side2 == 4
        assert triangle.side3 == 5

    def test_negative_side_raises_error(self):
        """Тест отрицательной стороны"""
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(-1, 2, 3)
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(1, -2, 3)
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(1, 2, -3)

    def test_zero_side_raises_error(self):
        """Тест нулевой стороны"""
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(0, 2, 3)
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(2, 0, 3)
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(2, 3, 0)

    def test_triangle_inequality_violation(self):
        """Тест нарушения неравенства треугольника"""
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(1, 2, 10)  # 1 + 2 < 10
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(2, 3, 5)  # 2 + 3 = 5
        with pytest.raises(ValueError, match="Invalid triangle sides"):
            Triangle(10, 1, 2)  # 1 + 2 < 10

    def test_equilateral_triangle_creation(self):
        """Тест создания равностороннего треугольника"""
        triangle = Triangle(5, 5, 5)
        assert triangle.side1 == 5
        assert triangle.side2 == 5
        assert triangle.side3 == 5


class TestTriangleMethods:
    """Тесты методов треугольника"""

    def test_get_sides(self):
        """Тест метода get_sides"""
        triangle = Triangle(3, 4, 5)
        sides = triangle.get_sides()
        assert sides == (3, 4, 5)
        assert isinstance(sides, tuple)

    def test_perimeter_calculation(self):
        """Тест вычисления периметра"""
        triangle = Triangle(3, 4, 5)
        assert triangle.perimeter() == 12

        triangle2 = Triangle(5.5, 6.5, 7.5)
        assert triangle2.perimeter() == 19.5

    def test_area_right_triangle(self):
        """Тест площади прямоугольного треугольника"""
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0  # (3*4)/2
        assert triangle.area() == pytest.approx(expected_area, abs=1e-10)

    def test_area_equilateral_triangle(self):
        """Тест площади равностороннего треугольника"""
        triangle = Triangle(4, 4, 4)
        expected_area = (math.sqrt(3) / 4) * 16  # (√3/4) * a²
        assert triangle.area() == pytest.approx(expected_area, abs=1e-10)

    def test_area_scalene_triangle(self):
        """Тест площади разностороннего треугольника"""
        triangle = Triangle(5, 6, 7)
        s = (5 + 6 + 7) / 2
        expected_area = math.sqrt(s * (s - 5) * (s - 6) * (s - 7))
        assert triangle.area() == pytest.approx(expected_area, abs=1e-10)

    def test_area_degenerate_triangle(self):
        """Тест площади почти вырожденного треугольника"""
        triangle = Triangle(1, 1, 1.999)
        area = triangle.area()
        assert area > 0
        assert area < 0.1  # Площадь должна быть очень маленькой



class TestTriangleProperties:
    """Тесты свойств треугольника"""

    def test_is_right_triangle(self):
        """Тест прямоугольных треугольников"""
        right_triangles = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
        for sides in right_triangles:
            triangle = Triangle(*sides)
            assert triangle.is_right() == True

        non_right_triangles = [(3, 4, 6), (5, 5, 5), (5, 6, 7)]
        for sides in non_right_triangles:
            triangle = Triangle(*sides)
            assert triangle.is_right() == False

    def test_is_equilateral_triangle(self):
        """Тест равносторонних треугольников"""
        equilateral = Triangle(5, 5, 5)
        assert equilateral.is_equilateral() == True

        almost_equilateral = Triangle(5, 5, 5.0001)
        assert almost_equilateral.is_equilateral() == False

        scalene = Triangle(3, 4, 5)
        assert scalene.is_equilateral() == False

    def test_is_isosceles_triangle(self):
        """Тест равнобедренных треугольников"""
        isosceles_cases = [
            (5, 5, 6),  # a = b
            (5, 6, 5),  # a = c
            (6, 5, 5),  # b = c
            (5, 5, 5),  # все равны
        ]
        for sides in isosceles_cases:
            triangle = Triangle(*sides)
            assert triangle.is_isosceles() == True

        scalene_cases = [(3, 4, 5), (5, 6, 7), (2, 3, 4)]
        for sides in scalene_cases:
            triangle = Triangle(*sides)
            assert triangle.is_isosceles() == False

    def test_property_combinations(self):
        triangle = Triangle(1, 1, math.sqrt(2))
        assert triangle.is_right() and triangle.is_isosceles()


class TestTriangleEdgeCases:
    """Тесты граничных случаев"""
    def test_large_triangle(self):
        """Тест большого треугольника"""
        triangle = Triangle(1000, 1000, 1000)
        assert triangle.perimeter() == 3000
        assert triangle.area() > 100000

    def test_floating_point_triangle(self):
        """Тест треугольника с числами с плавающей точкой"""
        triangle = Triangle(3.5, 4.2, 5.1)
        perimeter = triangle.perimeter()
        assert perimeter == pytest.approx(12.8, abs=1e-10)
        assert triangle.area() > 0
