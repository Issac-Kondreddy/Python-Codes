# Comprehensive Example of Exception Handling in Python

# This script combines try, except, finally, and raising an exception in a comprehensive example.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Dividing by zero is not allowed.")
    else:
        print(f"The result is {result}")
    finally:
        print("Executing finally clause...")

# Test the function
divide(10, 2)
divide(10, 0)

# Attempt to raise a custom exception
try:
    divide("10", "2")
except TypeError:
    print("TypeError: Non-numeric inputs not allowed.")

# This comprehensive example shows a function designed to divide two numbers, handle exceptions, and clean up resources using a finally clause.
