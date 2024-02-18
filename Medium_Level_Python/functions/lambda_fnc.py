# Lambda Functions in Python

# A simple lambda function that adds two numbers
add = lambda a, b: a + b

print(f"The sum of 10 and 20 is: {add(10, 20)}")

# Lambda functions are anonymous functions defined with the lambda keyword.
# They are used for creating small, one-time, and inline function objects in Python.

# Example using lambda function with filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: (x%2 == 0), numbers))
print(f"Even numbers: {even_numbers}")

# This script demonstrates defining and using lambda functions for simple operations and with filter().
