# if-else Statements in Python

# The if statement is used to test a specific condition. If the condition is true, a block of code (if-block) will be executed.
# If the condition is false, an optional else block of code can be executed.

# Basic if-else statement
age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Using elif for multiple conditions
# The elif (short for else if) statement allows you to check multiple expressions for TRUE and execute a block of code as soon as one of the conditions evaluates to TRUE.
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Nested if statements
# You can also nest if statements within another if statement.
num = -5
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# Conditional expressions (Python's ternary operator)
# Python supports a conditional expression that can be used as a shorthand for the if-else statement.
# Syntax: [on_true] if [expression] else [on_false]
can_vote = "Yes" if age >= 18 else "No"
print(f"Can vote? {can_vote}")

# The if-else statement is very versatile and can be used in various scenarios, from simple condition checking to complex logic with multiple conditions.
