# Logical Operators in Python

# The logical operators in Python are used to combine conditional statements:
# and, or, not

# Logical AND (and)
# Returns True if both the operands are true
x, y = True, False
print(f'{x} and {y}: {x and y}')  # Outputs: False because y is False

# Logical OR (or)
# Returns True if either of the operands is true
print(f'{x} or {y}: {x or y}')  # Outputs: True because at least one operand, x, is True

# Logical NOT (not)
# Reverses the logical state of its operand. If a condition is True, then Logical NOT operator will make it False.
print(f'not {x}: {not x}')  # Outputs: False because x is True

# These operators are typically used to evaluate boolean expressions, for example, in conditional statements like if, while.
