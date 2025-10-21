import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for at least one digit
    if not re.search(r"\d", password):
        return "Weak: Password must include at least one number."
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must include at least one uppercase letter."
    
    # Check for at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must include at least one special character."
    
    return "Strong Password ✅"

# Ask user for password input
password = input("Enter your password: ")

# Check and print result
print(check_password_strength(password))
