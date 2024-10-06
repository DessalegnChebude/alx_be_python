import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        # creating the object calc from the class of SimpleCalculator
        self.calc = SimpleCalculator()

    def test_addition(self):
        # Test the add method
        self.assertEqual(self.calc.add(3, 7), 10, "Should be 9")
        self.assertEqual(self.calc.add(-3, 8), 5, "should be 5")
        self.assertEqual(self.calc.add(-3, -5), -8, "should be -8")
        with self.assertRaises(TypeError):
            self.calc.add("a string", 7)

    def test_subtraction(self):
        # Test the subtract method
        self.assertEqual(self.calc.subtract(10, 4), 6, "should be 6")
        self.assertEqual(self.calc.subtract(3, 7), -4, "Should be -4")
        self.assertEqual(self.calc.subtract(-3, 8), -11, "should be -11")
        self.assertEqual(self.calc.subtract(-3, -5), 2, "should be -8")
        with self.assertRaises(TypeError):
            self.calc.add("a string", 2)
    
    def test_multiplication(self):
        # Test the subtract method
        self.assertEqual(self.calc.multiply(10, 4), 40, "should be 40")
        self.assertEqual(self.calc.multiply(3, 0), 0, "Should be 0")
        self.assertEqual(self.calc.multiply(-3, 8), -24, "should be -24")
        self.assertEqual(self.calc.multiply(-3, -5), 15, "should be 15")
        with self.assertRaises(TypeError):
            self.calc.add("a string", 2)

    def test_division(self):
        # Test the subtract method
        self.assertEqual(self.calc.divide(10, 4), 2.5, "should be 2.5")
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
        self.assertEqual(self.calc.divide(-16, 8), -2, "should be -24")
        self.assertEqual(self.calc.divide(-30, -5), 6, "should be 15")
        with self.assertRaises(TypeError):
            self.calc.add("a string", 2)
    

if __name__ == "__main__":
    unittest.main()
