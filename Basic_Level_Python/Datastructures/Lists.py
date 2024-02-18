
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]
print("Numbers:", numbers)

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Creating a mixed list
mixed = [1, "apple", True, 3.14]
print("Mixed:", mixed)

# Creating a nested list
nested = [1, [2, 3], ["apple", "banana"]]
print("Nested:", nested)

# Accessing the first item
print("First fruit:", fruits[0])

# Accessing the last item
print("Last fruit:", fruits[-1])

# Accessing a nested list item
print("Nested list item:", nested[1][0])

# Slicing from the start to the 3rd element
print("First three numbers:", numbers[:3])

# Slicing from the 3rd element to the end
print("From the third onward:", numbers[2:])

# Slicing with a negative index
print("Last two fruits:", fruits[-2:])

# Changing an element
numbers[0] = 10
print("Changed numbers:", numbers)

# Adding elements
fruits.append("orange")
print("Added fruit:", fruits)

# Removing elements
fruits.remove("banana")
print("Removed fruit:", fruits)

# Extending a list with another list
extras = ["grape", "pineapple"]
fruits.extend(extras)
print("Extended fruits:", fruits)
# List comprehension for squares of numbers
squares = [x**2 for x in numbers]
print("Squares:", squares)

# Filtering with list comprehension
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Sorting lists
sorted_fruits = sorted(fruits)
print("Sorted fruits:", sorted_fruits)

# Reversing a list
fruits.reverse()
print("Reversed fruits:", fruits)

# Finding the index of an element
index = fruits.index("apple")
print("Index of apple:", index)

# Counting occurrences of an element
count = fruits.count("apple")
print("Count of apple:", count)

