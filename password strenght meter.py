import re

def check_password_strength(password):
    # Minimum password length
    min_length = 8

    # Regular expression patterns
    lowercase = re.compile(r'[a-z]')
    uppercase = re.compile(r'[A-Z]')
    digits = re.compile(r'\d')
    special_chars = re.compile(r'[@$!%*?&]')
    
    # Strength score starts at 0
    score = 0

    # Check password length
    if len(password) >= min_length:
        score += 1
    
    # Check for lowercase letters
    if lowercase.search(password):
        score += 1
    
    # Check for uppercase letters
    if uppercase.search(password):
        score += 1
    
    # Check for digits
    if digits.search(password):
        score += 1
    
    # Check for special characters
    if special_chars.search(password):
        score += 1

    # Determine strength based on score
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Medium"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Test the password strength meter
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
