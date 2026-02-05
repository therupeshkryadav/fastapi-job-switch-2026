"""Simple interactive script.

Asks the user for their name, age, and favorite color, then prints
an estimated year of birth and echoes the favorite color.
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
# Note: float() may raise ValueError if the input isn't a valid number; consider
# validating input or catching exceptions to handle bad input gracefully.
weight_kg = float(input("Enter your weight in kilograms (e.g. 70.5): "))
# Convert kg to pounds (approx): 1 kg = 2.20462 lb
weight_lb = weight_kg * 2.20462
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

# Demonstrate string indexing: strings are sequences of characters and are
# indexed starting at 0. Accessing course[4] returns the fifth character.
course = "Python Learning"
# This will print the character at index 4 (0-based index), which is 'o'
print(course[4])