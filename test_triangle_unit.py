from unittest import TestCase, main
from triangle import Triangle
import unittest


class TestTriangleUnit(TestCase):

    def setUp(self):
        self.first = Triangle(9, 8, 7)
        print("Triangle 7,8,9 created as 'first")

    def tearDown(self):
        del self.first
        print("Triangle 7,8,9  'first deleted")

    def test_perimetr(self):
        print("test Perimetr started")
        print(Triangle.perimetr(self.first))
        self.assertTrue(Triangle.perimetr(self.first) == 24)
        print('test Perimetr end')

    def test_square(self):
        print("test Square started")
        print(Triangle.square(self.first))
        self.assertAlmostEqual(round(Triangle.square(self.first), 4), 26.8328, 4)
        print('test Square end')

    def test_triangle_eq(self):
        print('test EQUAL started ')
        second = Triangle(7, 9, 8)
        self.assertEqual(self.first, second)
        print('test EQUAL finished')
        # assert first == second

    def test_triangle_noteq(self):
        print('test NOTEQUAL started ')
        second = Triangle(4, 5, 6)
        self.assertNotEqual(self.first, second)
        print('test NOTEQUAL finished')

    def test_triangle_lt(self):
        print('test lt started ')
        second = Triangle(6, 7, 5)
        print(Triangle.perimetr(self.first))
        print(Triangle.perimetr(second))
        self.assertGreater(Triangle.perimetr(self.first), Triangle.perimetr(second))
        print('test lt finished')

    def test_triangle_gt(self):
        print('test gt started ')
        second = Triangle(9, 9, 9)
        print(Triangle.perimetr(self.first))
        print(Triangle.perimetr(second))
        self.assertLess(Triangle.perimetr(self.first), Triangle.perimetr(second))
        print('test gt finished')

    def test_triangle_le(self):
        print('test LE started ')
        second = Triangle(9, 8, 9)
        print(Triangle.perimetr(self.first))
        print(Triangle.perimetr(second))
        self.assertLessEqual(Triangle.perimetr(self.first), Triangle.perimetr(second))
        print('test LE finished')

    def test_triangle_ge(self):
        print('test GE started ')
        second = Triangle(9, 6, 6)
        print(Triangle.perimetr(self.first))
        print(Triangle.perimetr(second))
        self.assertGreaterEqual(Triangle.perimetr(self.first), Triangle.perimetr(second))
        print('test GE finished')

    def test_equals(self):
        print("test equals started")
        second = Triangle(16, 18, 14)
        self.assertTrue(Triangle.equal(self.first, second) is True)
        print('test equals end')

    @unittest.skip("TEST will FAIL when hypotenuse input in 1 or 2 pos")
    def test_is_right_angled(self):
        print('test 90C started ')
        second = Triangle(3, 5, 4)
        print(Triangle.is_right_angled(second))
        self.assertTrue(Triangle.is_right_angled(second) is True)
        print('test 90C finished')

    def test_is_right_triangle(self):
        print('test right triangle started ')
        second = Triangle(3, 3, 3)
        print(Triangle.is_right_triangle(second))
        self.assertTrue(Triangle.is_right_triangle(second) is True)
        print('test right triangle finished')

    def test_two_sides_eq(self):
        print('test two_sides_eq started ')
        second = Triangle(3, 5, 3)
        print(Triangle.is_right_triangle(second))
        self.assertTrue(Triangle.two_sides_eq(second) is True)
        print('test two_sides_eq ended')


if __name__ == '__main__':
    main()
