# 1. ARRANGE
# 2. ACT
# 3. INSERT

import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(10, add(6, 4))

    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))

    def test_multiply(self):
        self.assertEqual(25, multiply(5, 5))

    def test_divide(self):
        self.assertEqual(6, divide(36, 6))