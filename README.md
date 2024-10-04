# 🔒 Password Strength Checker  | [YouTube Video](https://www.youtube.com/watch?v=rF9PwboFnDU)

A Python-based password strength checker that evaluates the strength and complexity of a password using specific rules, provides feedback for improvement, calculates entropy, and estimates the time required for a brute-force attack.


## 📑 Table of Contents
- Features
- Requirements
- How It Works
  - Password Evaluation
  - Entropy Calculation
  - Time to Crack
  - Common Password Check
- Usage
- Example Output
- Future Enhancements
- Contributing

## 🚀 Features
- ✅ Checks if a password meets basic security criteria (length, uppercase, lowercase, numeric, special characters).
- 🔐 Calculates password entropy to assess complexity.
- 🕑 Estimates the time to brute-force the password.
- 🗂️ Checks against a list of common passwords to ensure uniqueness.

## 📋 Requirements
- Python 3.x
- Standard Python libraries: `re` (regular expressions), `math`
- A `common_passwords.txt` file for common password checks

## ⚙️ How It Works

### 🛡️ Password Evaluation
The script checks if the password meets the following criteria:
1. Minimum length of 12 characters.
2. Contains at least one uppercase letter.
3. Contains at least one lowercase letter.
4. Includes at least one number.
5. Has at least one special character.

If any of these criteria are not met, the user will receive feedback.

### 🧮 Entropy Calculation
Password entropy is calculated using the formula:


Entropy = log2(character_set^password_length)

Where `character_set` represents the number of possible characters in the password. Based on the entropy value, the password is classified as:

- **Very Strong** (Entropy > 128 bits)
- **Strong** (Entropy 60-127 bits)
- **Moderate** (Entropy 36-59 bits)
- **Weak** (Entropy 28-35 bits)
- **Very Weak** (Entropy < 28 bits)

### ⏳ Time to Crack
The time to crack the password is estimated based on brute-force attacks. Assuming a machine can test 1 billion passwords per second, the script displays the time in years, days, hours, minutes, and seconds.

### 🔍 Common Password Check
The password is checked against a list of common passwords (`common_passwords.txt`). If found, the script advises the user to select a more secure password.

## 💻 Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
2. Navigate to the project directory:
   ```bash
   cd password-strength-checker
3. Run the script:
   ```bash
   python password_strength_checker.py
   
📝 Example Output
4. Enter a password when prompted.
   ```dif
   please enter a password to check strength: 
   please enter a password to check strength: 
   P@ssw0rd!
   -> Password length should be at least 12 characters.
   -> Password complexity is: Moderate
   -> password Entropy: 56.73 bits
   -> Estimated time to crack the password by brute force with high performance machine:
   -> 3 years, 292 days, 4 hours, 6 minutes, 35 seconds
```

🚀 Future Enhancements
  - Improve the feedback by suggesting how to increase the entropy further.
  - Add more common password datasets for enhanced uniqueness checks.
  - Implement a graphical user interface (GUI) for easier interaction.
  
🤝 Contributing
  - Feel free to contribute by submitting issues or pull requests if you find a bug or have an idea for a new feature.
