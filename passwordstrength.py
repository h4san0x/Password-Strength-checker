import string

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1

if len(password) >= 12:
    score += 1

# Check lowercase
if any(char.islower() for char in password):
    score += 1

# Check uppercase
if any(char.isupper() for char in password):
    score += 1

# Check number
if any(char.isdigit() for char in password):
    score += 1

# Check special character
if any(char in string.punctuation for char in password):
    score += 1

# Common passwords
common_passwords = ["password", "123456", "qwerty", "admin", "password123"]

if password.lower() in common_passwords:
    score = 0

# Display strength
if score <= 2:
    print("Weak password")
elif score <= 4:
    print("Medium password")
else:
    print("Strong password")