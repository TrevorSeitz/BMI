import unittest
from unittest import result
from unittest.mock import patch, Mock
from unittest import TestCase
import BMI_Calculator 
import Calculate

class TestBMI(TestCase):
    print("printing from TestBMI")
    @patch('Calculate.input', create=True)
    def test_bmi(self):
        # mocked_input.side_effect = [60, 1.90]
        # height = mocked_input()
        # weight = mocked_input()
        bmi = 16.6
        result = BMI_Calculator.calculate(60, 1.90)
        self.assertEqual(result, bmi)
    test_bmi()

    
    
# class DictCreateTests(TestCase):
#     @mock.patch('module_under_test.input', create=True)
#     def testdictCreateSimple(self, mocked_input):
#         mocked_input.side_effect = ['Albert Einstein', '42.81', 'done']
#         result = dictCreate(1)
#         self.assertEqual(result, {'Albert Einstein': [42.81]})