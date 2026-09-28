import string
from getpass import getpass

def check_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Check special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character.")

    # Determine password strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


print("=" * 40)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = getpass("Enter your password: ")


strength, suggestions = check_password(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("\nYour password meets all basic requirements!")