import unittest
from password_strength_checker import evaluate_password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_weak_password(self):
        self.assertEqual(evaluate_password_strength("12345"), "Weak")

    def test_moderate_password(self):
        self.assertEqual(evaluate_password_strength("abc123ABC"), "Moderate")

    def test_strong_password(self):
        self.assertEqual(evaluate_password_strength("Str0ng@Pass"), "Strong") 

if __name__ == "__main__":
    unittest.main()
