"""Simple interactive script demonstrating basic I/O and string ops.

This small script interacts with the user via the terminal: it asks for
the user's name, age, favorite color and weight, then prints friendly
responses. It's intended as an educational example for beginners to show
how to read input, convert types, format output, and perform simple
string operations in Python.

Notes:
- Inputs from `input()` are returned as strings; conversions (e.g. to
	`int` or `float`) are necessary for numeric operations and may raise
	exceptions on invalid input. In production code, validate inputs or
	handle exceptions to re-prompt users.
"""

from datetime import date

# Ask for the user's name (stored as a string)
name = input("Enter your name: ")

# Ask for the user's age and convert the response to an integer.
# Converting here allows arithmetic operations on the age value.
# Note: converting user input with int() will raise ValueError if the input
# isn't a valid integer. In production code you should validate input or
# catch exceptions and re-prompt the user for correct input.
age = int(input("Enter your age: "))

# Ask for the user's favorite color (stored as a string)
color = input("Enter your favorite color: ")

# Compute an approximate year of birth using the current year.
# Note: this assumes the user has already had their birthday this year.
# If you want an exact birth year, ask for the birth date (year/month/day)
# and compute accordingly.
year_of_birth = date.today().year - age

# Output a friendly message using an f-string (formatted string literal)
# which interpolates the variables directly into the string.
print(f"Hello, {name}! You were born in {year_of_birth}. Your favorite color is {color}.")

# Ask for the user's weight in kilograms, convert to pounds and print nicely.
# Use float to allow fractional weights and format the output for readability.
# Note: `float()` may raise ValueError for invalid input; consider
# validating input or catching exceptions to handle bad input gracefully.
weight_kg = float(input("Enter your weight in kilograms (e.g. 70.5): "))
# Conversion constant for kilograms to pounds. Defining a named constant
# makes the conversion clearer and easier to change or reuse.
KG_TO_LB = 2.20462
weight_lb = weight_kg * KG_TO_LB
# Format specifiers used below:
# - {weight_kg:.1f}: show kilograms with one decimal place
# - {weight_lb:.2f}: show pounds with two decimal places
print(f"Thanks, {name}! Your weight is {weight_kg:.1f} kg (~{weight_lb:.2f} lb).")

# Demonstrate string quoting rules when text contains an apostrophe:
# - Python supports both single ('...') and double ("...") quoted strings.
# - If the string contains an apostrophe (single quote), using double quotes
#   avoids the need for escaping. For example:
#     print("Python's class goes fine!")
#   Alternatively, you can escape the apostrophe inside single quotes:
#     print('Python\'s class goes fine!')
# Here we use double quotes for readability.
print("Python's class goes fine!")
# Using single quotes here requires escaping the apostrophe (\') but lets us
# include double quotes inside the string without escaping, which can improve
# readability when quoting words inside the string.
print('Python\'s class "goes" fine!')

# For long, multi-line messages use triple-quoted strings (''' or """).
# Triple-quoted strings preserve newlines and are easier to read and maintain
# than trying to embed literal newlines inside single-quoted strings.
# Use an f-string here so the `name` variable entered earlier is included
# instead of a hard-coded name.
message = f'''Hi {name},

This is the founder of the unicorn company who wants to talk to you. Please
connect with me as soon as possible.

Thank you
'''
print(message)

# ----------------------------
# STRING CONCATENATION EXAMPLES
# ----------------------------
# String concatenation means joining strings together. There are several ways:

# Method 1: Using the + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"\n--- String Concatenation ---")
print(f"Using + operator: {full_name}")

# Method 2: Using f-strings (modern, recommended)
greeting = f"Hello, {first_name} {last_name}!"
print(f"Using f-string: {greeting}")

# Method 3: Using .join() method with a list of strings
words = ["Welcome", "to", "Python", "programming"]
sentence = " ".join(words)
print(f"Using .join(): {sentence}")

# ----------------------------
# LEN() FUNCTION EXAMPLES
# ----------------------------
# The len() function returns the number of characters in a string.

print(f"\n--- len() Function ---")
test_string = "Python"
print(f"len('{test_string}') = {len(test_string)}")

# Count characters including spaces and punctuation
test_message = "Hello, World!"
print(f"len('{test_message}') = {len(test_message)}")

# Practical use: validate password length
password = input("Enter a password to validate: ")
password_length = len(password)
print(f"Your password has {password_length} characters.")
if password_length >= 8:
    print("✓ Strong password (8+ characters)")
else:
    print("✗ Weak password (less than 8 characters)")

# Combine concatenation and len()
info = f"Welcome {name}! Your name '{name}' has {len(name)} letters."
print(f"\nCombined example: {info}")

# Demonstrate string indexing and slicing. Strings are sequences of
# characters and follow 0-based indexing. Slicing `start:end` returns a
# substring from `start` up to but not including `end`.
course = "Python Learning"
#         0123456789.....
# Individual character access (index 4 -> fifth character):
print(course[4])

# Common slicing patterns:
print(course[0:11])   # characters 0 through 10 (11 chars)
print(course[:11])    # same as above, start defaults to 0
print(course[7:])     # from index 7 to the end of the string

# Demonstrate how to inspect the runtime type of a variable using `type()`.
# This prints the Python type objects for several variables collected above.
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of weight_kg:", type(weight_kg))
print("Type of weight_lb:", type(weight_lb))
print("Type of course:", type(course))
# ----------------------------
# Operator examples: arithmetic, relational, assignment, logical
# ----------------------------
print("\n--- Operator examples ---")
a = -10
b = 3

# Arithmetic operators
print("Arithmetic operators:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# Relational (comparison) operators
print("\nRelational (comparison) operators:")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Assignment operators
print("\nAssignment operators:")
c = a
print(f"c = {c}")
c += b
print(f"c += {b} -> {c}")
c *= 2
print(f"c *= 2 -> {c}")
c %= 5
print(f"c %= 5 -> {c}")

# Logical operators
print("\nLogical operators:")
x = True
y = False
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# Combining relational and logical operators
print("\nCombined expressions:")
age_check = age >= 18
print(f"age >= 18 and weight_kg > 50: {age_check and weight_kg > 50}")
print(f"(age < 30) or (weight_kg < 60): {(age < 30) or (weight_kg < 60)}")