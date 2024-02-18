# Dictionaries in Python: A Comprehensive Guide

# Creating a Dictionary
# Dictionaries are created by placing a comma-separated list of key:value pairs within braces {}, with keys and values separated by a colon.
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict)

# Accessing Elements
# You can access the value associated with a specific key using square brackets [] or the get() method.
print(my_dict['name'])  # Outputs: John
print(my_dict.get('age'))  # Outputs: 30

# Adding or Modifying Elements
# Dictionaries are mutable, meaning you can add new key:value pairs or change the value associated with an existing key.
my_dict['email'] = 'john@example.com'  # Adds a new key:value pair
my_dict['age'] = 31  # Updates the value for the key 'age'
print(my_dict)

# Removing Elements
# Use del to remove a key:value pair by key, or pop() to remove it and return the value.
del my_dict['city']  # Removes the key 'city' along with its value
print(my_dict)
age = my_dict.pop('age')  # Removes 'age' and returns its value
print(f"Removed age: {age}")
print(my_dict)

# Keys, Values, and Items
# dict.keys() returns a view object displaying a list of all the keys, dict.values() for all the values, and dict.items() for all key:value pairs.
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# Iterating Through a Dictionary
# You can iterate through a dictionary using a loop, accessing keys, values, or both.
for key in my_dict:
    print(key, my_dict[key])  # Prints keys and their corresponding values

for key, value in my_dict.items():
    print(key, value)  # Another way to print keys and values

# Nested Dictionaries
# Dictionaries can contain other dictionaries, lists, or any other data types, allowing complex data structures.
nested_dict = {
    'dict1': {'value': 1},
    'dict2': ['list', 'in', 'a', 'dict'],
    'dict3': 'Just a string'
}
print(nested_dict)

# Dictionary Comprehensions
# Similar to list comprehensions, dictionary comprehensions allow you to create dictionaries from arbitrary key and value expressions.
squared_numbers = {x: x**2 for x in range(6)}
print(squared_numbers)

# Why Use Dictionaries?
# Dictionaries are ideal for storing and accessing data where the relationship between each element (the key) and its value is significant. They're especially useful for fast lookup operations, storing configurations, and managing complex data.

