import math
import unittest
from geometry import Circle, Triangle, calculate_area


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=2)
        self.assertAlmostEqual(circle.area(), 12.566370614359172, places=6)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=6)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_non_right_triangle(self):
        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_right())

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_invalid_triangle_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_calculate_area_function(self):
        circle = Circle(1)
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(circle), math.pi, places=6)
        self.assertAlmostEqual(calculate_area(triangle), 6.0, places=6)


if __name__ == '__main__':
    unittest.main()
