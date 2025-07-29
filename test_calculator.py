#https://github.com/racolas1/lab10-NL
# Partner 1: Nikolas Lima
# Partner 2: Nikolas Lima
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(3, -1), 2)
        self.assertEqual(add(5.4, 1.8), 7.2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(add(4, 5), -1)
        self.assertEqual(add(3, -1), 4)
        self.assertEqual(add(5.4, 1.8), 3.6)

    def test_multiply(self): # 3 assertions
        self.assertEqual(add(4, 5), 20)
        self.assertEqual(add(3, -1), -3)
        self.assertEqual(add(5.4, 1.8), 9.72)

    def test_divide(self): # 3 assertions
        self.assertEqual(add(4, 4), 1)
        self.assertEqual(add(-1, 3), -3)
        self.assertEqual(add(6, 3), 0.5)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(10, 1000), 3)
        self.assertEqual(log(0.5, 2), -1)
        self.assertEqual(log(2, 2), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(2, 1)
            log(0.5, 0)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(0,0), 0)
        with self.assertRaises(TypeError):
            hypotenuse("hello")

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(TypeError):
            square_root("hello")
        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()