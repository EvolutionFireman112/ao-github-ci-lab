"""Unit tests for the isolated AO GitHub CI pilot."""

import unittest

from sum_values import add_numbers


class AdditionTests(unittest.TestCase):
    def test_known_total(self):
        self.assertEqual(add_numbers(250, 250), 500)

    def test_negative_number(self):
        self.assertEqual(add_numbers(-20, 50), 30)


if __name__ == "__main__":
    unittest.main()
