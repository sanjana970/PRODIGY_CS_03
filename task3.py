import re

def assess_password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    numbers = any(char.isdigit() for char in password)
    special_chars = re.search(r'[!@#$%^&*()-_=+]', password) is not None

    strength = 0
    feedback = []

    if length >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase and lowercase:
        strength += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    if numbers:
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_chars:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    if strength >= 4:
        feedback.append("Password is strong.")
    elif strength >= 2:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is weak.")

    return feedback

def main():
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    for message in feedback:
        print(message)

if _name_ == "_main_":
    main()