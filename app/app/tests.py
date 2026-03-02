"""
Sample tests for the application.
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """Test that the add function returns the correct sum."""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)

    def test_add_strings(self):
        """Test that the add function concatenates strings."""
        res = calc.add("Hello, ", "World!")
        self.assertEqual(res, "Hello, World!")
