# Writing to Files in Python

# Opening a file for writing. If the file exists, this will overwrite it.
file = open('../file_handling/example', 'w')

# Writing a string to the file
file.write("Hello, Python file handling!")

# Closing the file is important to ensure data is physically written to disk
file.close()

# Appending text to an existing file
file = open('../file_handling/example', 'a')  # 'a' mode opens the file for appending
file.write("\nAppending a new line to the file.")
file.close()

# This script demonstrates how to write and append text to files in Python.
