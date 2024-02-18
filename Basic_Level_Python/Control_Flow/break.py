# Break Statement in Python

# The break statement is used to break out of the loop when a condition becomes true during its execution.

# Example using break in a for loop
for num in range(10):
    if num == 5:
        break  # Loop stops when num reaches 5
    print(num)

# Example using break in a while loop
count = 0
while count < 10:
    if count == 6:
        break
    print(count)
    count += 1

# The break statement provides a way to exit out of a loop when a specific condition is met.
