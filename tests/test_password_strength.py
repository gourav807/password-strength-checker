import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from password_strength_checker import evaluate_password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_01_weak_password(self):
        self.assertEqual(evaluate_password_strength("12345"), "Weak")

    def test_02_moderate_password(self):
        self.assertEqual(evaluate_password_strength("abc123ABC"), "Moderate")

    def test_03_strong_password(self):
        self.assertEqual(evaluate_password_strength("Str0ng@Pass"), "Strong")

if __name__ == "__main__":
    unittest.main()
