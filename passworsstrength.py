import re

def check_password_strength(password):
    # Define the criteria for a strong password
    min_length = 8
    has_upper = re.search(r'[A-Z]', password) is not None
    has_lower = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    is_long_enough = len(password) >= min_length

    # Check if all criteria are met
    if all([has_upper, has_lower, has_digit, has_special, is_long_enough]):
        return "Strong password"
    else:
        return "Weak password"

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(strength)
