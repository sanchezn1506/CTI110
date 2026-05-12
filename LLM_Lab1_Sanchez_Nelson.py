#  Nelson Sanchez
#  LLM Lab 1
#  4/12/2026
#  Password Generator

#  Chat gpt promt: create python code for a random password generator. Make the password 16 characters long containing at least one capital letter one lower case letter and one special character.

import secrets
import string

def generate_password(length=16):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    # Remove ambiguous characters
    uppercase_letters = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # removed O
    lowercase_letters = "abcdefghijkmnopqrstuvwxyz"  # removed l
    digits = "23456789"  # removed 0 and 1
    special_chars = "!@#$%^&*()-_=+[]{};:,.<>?"

    # Ensure at least one from each category
    password = [
        secrets.choice(uppercase_letters),
        secrets.choice(lowercase_letters),
        secrets.choice(digits),
        secrets.choice(special_chars),
    ]

    # Fill the rest
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    password += [secrets.choice(all_chars) for _ in range(length - 4)]

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

# Generate password
pwd = generate_password()

# Print in green (ANSI escape code)
print("\033[92m" + pwd + "\033[0m")