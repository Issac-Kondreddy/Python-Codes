# Function Arguments in Python

def introduce(name, age=30):
    """
    This function introduces a person with a given name and age.

    Parameters:
    name (str): The name of the person.
    age (int, optional): The age of the person. Defaults to 30.

    Returns:
    None
    """
    print(f"My name is {name} and I am {age} years old.")


# Positional arguments
introduce('John', 25)

# Keyword arguments
introduce(age=22, name='Jane')

# Default arguments
introduce('Mike')

# This function demonstrates the use of positional, keyword, and default arguments.
