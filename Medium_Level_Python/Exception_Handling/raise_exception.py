# Raising Exceptions in Python

# You can raise exceptions using the raise statement.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        print("You are not eligible to vote.")
    else:
        print("You are eligible to vote.")

try:
    check_age(-1)
except ValueError as e:
    print(e)

# This script demonstrates raising an exception with a custom error message and catching it in a try-except block.
