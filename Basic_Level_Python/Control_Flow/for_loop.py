# For Loops in Python

# A for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.

# Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Using the range() function
for i in range(5):  # Starts from 0 by default, up to but not including 5
    print(i)

# Nested for loops
# Using a nested for loop to iterate over a two-dimensional list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for item in row:
        print(item)

# The for loop in Python is powerful and versatile, allowing you to iterate over the elements of a sequence or any iterable object.
