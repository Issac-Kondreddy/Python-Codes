# Booleans.py

# Boolean values: True or False
print("Boolean Values:")
is_active = True
is_registered = False

print("Is Active:", is_active)
print("Is Registered:", is_registered)

# Comparison operations result in boolean values
print("\nComparison Operations:")
a = 10
b = 20

print("a == b (is equal):", a == b)  # Equal
print("a != b (is not equal):", a != b)  # Not equal
print("a < b (is less than):", a < b)  # Less than
print("a > b (is greater than):", a > b)  # Greater than
print("a <= b (is less than or equal to):", a <= b)  # Less than or equal to
print("a >= b (is greater than or equal to):", a >= b)  # Greater than or equal to

# Logical operations with boolean values
print("\nLogical Operations:")
print("True and False:", True and False)  # Logical AND
print("True or False:", True or False)  # Logical OR
print("not True:", not True)  # Logical NOT

# Using Boolean in control flow
print("\nUsing Boolean in Control Flow:")
if is_active:
    print("Account is active.")
else:
    print("Account is not active.")

# Boolean in conditional expressions
is_even = True if a % 2 == 0 else False
print("Is 'a' even?:", is_even)
