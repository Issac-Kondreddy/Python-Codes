# Importing Modules in Python

# Import the entire math module
import math

# Now you can use functions and variables defined in the math module
print(math.sqrt(16))  # Outputs: 4.0

# Import only specific attributes from a module
from datetime import datetime

# Use the datetime class directly without the module prefix
now = datetime.now()
print(f"Current date and time: {now}")

# Import a module with an alias
import statistics as stats

# Use the alias to access functions from the statistics module
data = [1, 2, 3, 4, 5, 6]
mean = stats.mean(data)
print(f"Mean of data: {mean}")

# This script demonstrates various ways to import modules and use their functionalities in Python.
