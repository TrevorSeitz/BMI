import unittest
from unittest import result
from unittest import TestCase
from Calculate import calculate

class TestBMI(TestCase):
    print("printing from TestBMI")
    def test_bmi(self):
        weight = 60
        height = 1.9
        bmi = 16.6
        self.assertEqual(calculate(weight, height), bmi)


if __name__ == "__main__":
    unittest.main()
    