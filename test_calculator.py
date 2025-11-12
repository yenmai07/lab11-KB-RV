#https://github.com/yenmai07/lab11-KB-RV.git
#Partner 1: Kayla Bui
#Partner 2: Rosetta Vang


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(18, 22), 40)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 6), 4)
        self.assertEqual(subtract(54, 3), 51)
        self.assertEqual(subtract(99, 4), 95)

    #Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(9, 3), 3)
        self.assertAlmostEqual(div(7, 2), 3.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(3, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 87), math.log(87,10))
        self.assertAlmostEqual(logarithm(8, 12), math.log(12, 8))
        self.assertAlmostEqual(logarithm(27, 10), math.log(10,27))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code
    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.414213, places=5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.414213, places=5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()