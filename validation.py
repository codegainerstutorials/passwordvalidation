import re

def is_valid_password(password):
    # At least 8 characters
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
     if len(password) > 19:
        return False, "Password is too long."
    # At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    # At least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    # At least one digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."
    # At least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."
    return True, "Password is valid."

if __name__ == "__main__":
    pwd = input("Enter a password to validate: ")
    valid, message = is_valid_password(pwd)
    while True:
        print(message)
        if valid:
            break
        pwd = input("Enter a password to validate: ")
        valid, message = is_valid_password(pwd)