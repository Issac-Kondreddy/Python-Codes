# Bitwise Operators in Python

# Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit:
# &, |, ^, ~, <<, >>

# Bitwise AND (&)
# Sets each bit to 1 if both bits are 1
a, b = 0b1010, 0b0101  # Binary literals for 10 and 5
print(f'{a} & {b}: {a & b}')  # Outputs: 0 (0b0000)

# Bitwise OR (|)
# Sets each bit to 1 if one of two bits is 1
print(f'{a} | {b}: {a | b}')  # Outputs: 15 (0b1111)

# Bitwise XOR (^)
# Sets each bit to 1 if only one of two bits is 1
print(f'{a} ^ {b}: {a ^ b}')  # Outputs: 15 (0b1111)

# Bitwise NOT (~)
# Inverts all the bits
print(f'~{a}: {~a}')  # Outputs: -11 (inverts all bits of 10, resulting in -11 due to two's complement representation)

# Bitwise Left Shift (<<)
# Shifts left by pushing zeros in from the right and let the leftmost bits fall off
print(f'{a} << 2: {a << 2}')  # Outputs: 40 (0b101000)

# Bitwise Right Shift (>>)
# Shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(f'{a} >> 2: {a >> 2}')  # Outputs: 2 (0b10)

# Bitwise operators are useful for tasks that involve flag manipulation, bit masks, and other operations where the binary representation of numbers is pertinent.
