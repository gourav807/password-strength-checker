
# 🛠️ Tool’s Working Process: Password Strength Checker

The **Password Strength Checker** is a Python-based script that evaluates the security strength of a user-provided password. It does so by checking if the password meets several key security criteria. Based on how many of these checks the password passes, it classifies the strength as **"Weak," "Moderate," or "Strong."**

### 🔄 Working Process (Step-by-Step)

1. **User Input:**  
   The program prompts the user to enter a password via the terminal.

2. **Password Evaluation:**  
   The input password is checked against five conditions:
   - Minimum length of 8 characters
   - Contains at least one uppercase letter
   - Contains at least one lowercase letter
   - Contains at least one digit
   - Contains at least one special character (e.g., `!@#$%^&*()`)

3. **Scoring Logic:**  
   For each satisfied condition, the program adds 1 point to a total score (out of 5). The final score determines the strength of the password.

4. **Feedback Output:**  
   The program prints a single word describing the strength:
   - **Weak** (0–2 conditions passed)
   - **Moderate** (3–4 conditions passed)
   - **Strong** (all 5 conditions passed)

---

## 🔑 Key Functions

### `evaluate_password_strength(password)`
- **Purpose:** Checks the password against all five criteria.
- **Input:** A string (password).
- **Returns:** A string — `"Weak"`, `"Moderate"`, or `"Strong"` based on the score.

### `main()`
- **Purpose:** Handles user interaction, takes input, calls the evaluation function, and prints the result.
- **Includes:** A `__main__` guard to ensure clean script execution.
