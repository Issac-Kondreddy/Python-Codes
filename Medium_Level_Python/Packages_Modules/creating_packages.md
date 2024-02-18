# Creating Packages in Python

A package in Python is a way of organizing related modules into a single directory hierarchy. Here's a basic guide on creating a package.

## Directory Structure

Consider a package named `mypackage` that contains two modules: `module1.py` and `module2.py`. The directory structure would look like this:


- `__init__.py`: This file makes Python treat the directories as containing packages. It can be empty or execute initialization code for the package.

## Creating a Simple Package

1. **Create the package directory**: Name it `mypackage`.
2. **Add modules**: Create `module1.py` and `module2.py` files within the `mypackage` directory.
3. **Initialize the package**: Create an empty `__init__.py` file in the `mypackage` directory.

## Using the Package

To use the package in your Python scripts:

```python
# Importing a module from the package
from mypackage import module1

# Using a function defined in module1
module1.my_function()
