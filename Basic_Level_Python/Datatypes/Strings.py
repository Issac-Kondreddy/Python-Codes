# Strings.py

# Creating strings
print("Creating Strings:")
hello_world = "Hello, World!"
print(hello_world)

# Accessing characters in a string
print("\nAccessing Characters:")
first_char = hello_world[0]
print("First Character:", first_char)
last_char = hello_world[-1]
print("Last Character:", last_char)

# Slicing strings
print("\nSlicing Strings:")
first_five = hello_world[:5]
print("First Five Characters:", first_five)
from_five = hello_world[5:]
print("From Fifth Character Onward:", from_five)

# Concatenating strings
print("\nConcatenating Strings:")
greeting = "Hello"
name = "Issac"
greeting_message = greeting + ", " + name + "!"
print("Greeting Message:", greeting_message)

# Common String Methods
print("\nCommon String Methods:")
print("Upper:", hello_world.upper())
print("Lower:", hello_world.lower())
print("Title:", hello_world.title())
print("Replace 'World' with 'Python':", hello_world.replace("World", "Python"))
print("Strip Exclamation:", hello_world.strip("!"))
print("Find 'World':", hello_world.find("World"))
print("Split by ',' :", hello_world.split(","))

# String formatting
print("\nString Formatting:")
age = 23
intro_message = f"My name is {name} and I am {age} years old."
print(intro_message)

# Checking string content
print("\nChecking String Content:")
print("Is 'hello_world' alphanumeric?", hello_world.isalnum())  # False due to punctuation and space
print("Is 'hello_world' alphabetic?", hello_world.isalpha())  # False due to punctuation and space
numeric_string = "12345"
print("Is 'numeric_string' numeric?", numeric_string.isnumeric())  # True

# Joining strings
print("\nJoining Strings:")
words = ["Hello", "world", "from", "Python"]
joined_string = " ".join(words)
print("Joined String:", joined_string)
