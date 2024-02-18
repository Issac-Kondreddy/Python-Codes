# While Loops in Python

# A while loop statement repeatedly executes a target statement as long as a given condition is true.

# Example of a simple while loop
count = 0
while count < 5:
    print(count)
    count += 1  # Important: This line prevents the loop from becoming infinite.

# Using else statement with while loop
# The else part is executed if the condition in the while loop evaluates to False.
count = 0
while count < 3:
    print(f"Inside loop: {count}")
    count += 1
else:
    print("In else block")

# Remember, the condition is checked before executing the loop body. If the condition never changes to False, you'll end up in an infinite loop.
