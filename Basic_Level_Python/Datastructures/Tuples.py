# Tuples in Python: An Overview

# Creating a Tuple
# Tuples are defined by enclosing the elements in parentheses `()`, separated by commas.
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# Accessing Tuple Elements
# You can access tuple elements using indexing, just like lists. Remember, indexing starts at 0.
print(my_tuple[1])  # Outputs: Hello

# Nested Tuples
# Tuples can contain other tuples (or lists) as elements, creating a nested structure.
nested_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(nested_tuple)

# Immutable Nature of Tuples
# Once a tuple is created, you cannot change its values. The following line would result in an error.
# my_tuple[1] = "Python"  # Uncommenting this line will raise a TypeError

# Tuple Unpacking
# Python allows you to unpack the tuple into variables.
a, b, c = my_tuple
print(a)  # Outputs: 1
print(b)  # Outputs: Hello
print(c)  # Outputs: 3.4

# Concatenation and Repetition
# You can concatenate tuples using the + operator, and repeat them using the * operator.
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
print(tuple1 + tuple2)  # Outputs: (1, 2, 3, 'a', 'b', 'c')
print(tuple1 * 3)       # Outputs: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Tuple Methods
# Tuples have built-in methods, but fewer than lists due to their immutability.
# count(x) - Returns the number of items x.
# index(x) - Returns the index of the first item that is equal to x.

print(my_tuple.count(1))  # Outputs: 1
print(my_tuple.index("Hello"))  # Outputs: 1

# Why Use Tuples?
# Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
# It makes your code safer if you “write-protect” data that does not need to be changed.
