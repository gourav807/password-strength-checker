# -*- coding: utf-8 -*-
"""password_strength_checker.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UpFk8elQN1Fa-8xLxwVuIGWQ5B8bWn02
"""

import re

def evaluate_password_strength(password):
    # Check each requirement
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password) is not None
    lower = re.search(r"[a-z]", password) is not None
    digit = re.search(r"\d", password) is not None
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Count how many checks passed
    score = sum([length, upper, lower, digit, special])

    # Return strength label
    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# Main program
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")
    strength = evaluate_password_strength(password)
    print(f"Password Strength: {strength}")