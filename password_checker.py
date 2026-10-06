from getpass import getpass

print("Password Strength Checker")
print("-------------------------")

password = getpass("Enter your password: ")

common_passwords = {
    "password",
    "123456",
    "12345678",
    "qwerty",
    "password123",
    "admin123"
}

if password.lower() in common_passwords:
    print("Warning: This is a common password.")

length = len(password)

print("Password length:", length)

if length < 8:
    print("Password is too short")
else:
    print("Password has acceptable length")

has_uppercase = any(char.isupper() for char in password)

if has_uppercase:
    print("Contains uppercase letter: Yes")
else:
    print("Contains uppercase letter: No")

has_number = any(char.isdigit() for char in password)

if has_number:
    print("Contains number: Yes")
else:
    print("Contains number: No")

symbols = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"

has_symbol = any(char in symbols for char in password)

if has_symbol:
    print("Contains symbol: Yes")
else:
    print("Contains symbol: No")

score = 0

if length >= 8:
    score += 1

if has_uppercase:
    score += 1

if has_number:
    score += 1

if has_symbol:
    score += 1


if password.lower() in common_passwords:
    strength = "Weak"
elif score <= 1:
    strength = "Weak"
elif score <= 3:
    strength = "Medium"
else:
    strength = "Strong"

print("-------------------------")
print("Password Strength:", strength)