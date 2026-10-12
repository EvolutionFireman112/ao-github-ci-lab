"""Deliberately failing test for the approved AO GitHub CI observer pilot.

This test is intentionally wrong. Its only purpose is to produce a failed
python-tests check in a separate, disposable lab PR. Do not merge this PR.
"""

import unittest

from sum_values import add_numbers


class IntentionalCIFailureTests(unittest.TestCase):
    def test_intentionally_wrong_expected_total(self):
        # The implementation correctly returns 500; 450 is deliberately wrong.
        self.assertEqual(
            add_numbers(250, 250),
            450,
            "Intentional failure for AO CI observation; no repair authorized",
        )


if __name__ == "__main__":
    unittest.main()
