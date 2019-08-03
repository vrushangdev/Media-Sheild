from django.test import TestCase
from calc import add,sub


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test That Two Numbers Are Added Together """
        self.assertEqual(add(3, 8), 11)


    def test_subtract_numbers(self):
        """Test Subtraction Of Two Values"""
        self.assertEqual(sub(5,2),3)