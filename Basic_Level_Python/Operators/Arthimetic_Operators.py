# Arithmetic Operators in Python

# Addition (+)
# Adds values on either side of the operator.
a = 10
b = 5
addition = a + b
print(f'Addition: {a} + {b} = {addition}')

# Subtraction (-)
# Subtracts right-hand operand from left-hand operand.
subtraction = a - b
print(f'Subtraction: {a} - {b} = {subtraction}')

# Multiplication (*)
# Multiplies values on either side of the operator
multiplication = a * b
print(f'Multiplication: {a} * {b} = {multiplication}')

# Division (/)
# Divides left-hand operand by right-hand operand. The result is a floating point number.
division = a / b
print(f'Division: {a} / {b} = {division}')

# Floor Division (//)
# The division of operands where the result is the quotient in which the digits after the decimal point are removed.
# But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity).
floor_division = a // b
print(f'Floor Division: {a} // {b} = {floor_division}')

# Modulus (%)
# Divides left-hand operand by right-hand operand and returns the remainder.
modulus = a % b
print(f'Modulus: {a} % {b} = {modulus}')

# Exponent (**)
# Performs exponential (power) calculation on operators.
exponent = a ** b
print(f'Exponent: {a} ** {b} = {exponent}')

# Understanding the results
# The addition, subtraction, multiplication, and modulus operations are straightforward.
# Division always results in a float, even if the division is evenly divisible.
# Floor division returns an integer result, discarding any fractional part, unless involved with floats where it behaves consistently with the division operator.
# The exponent operator raises the first number to the power of the second.

