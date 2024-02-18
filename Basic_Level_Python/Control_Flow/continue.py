# Continue Statement in Python

# The continue statement is used to skip the rest of the code inside a loop for the current iteration only.

# Example using continue in a for loop
for num in range(10):
    if num % 2 == 0:
        continue  # Skip print statement for even numbers
    print(num)

# Example using continue in a while loop
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)

# The continue statement stops the current iteration and proceeds with the next iteration of the loop.
