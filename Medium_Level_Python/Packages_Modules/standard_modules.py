# Exploring Standard Modules in Python

# The os module provides functions for interacting with the operating system
import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# The sys module provides access to some variables used or maintained by the Python interpreter
import sys

# Print Python version
print(f"Python version: {sys.version}")

# The random module provides tools for making random selections
import random

# Generate a random number between 1 and 100
rand_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {rand_num}")

# The json module provides a way to encode and decode JSON data
import json

# Convert Python dictionary to a JSON string
person_dict = {"name": "John", "age": 30, "city": "New York"}
person_json = json.dumps(person_dict)
print(f"JSON representation: {person_json}")

# This script showcases the use of some standard modules that come with Python and their basic functionalities.
