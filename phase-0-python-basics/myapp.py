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

# Get user inputs
name = input("Enter your name: ")

# Convert age to int for arithmetic operations
# Note: int() raises ValueError on invalid input—validate in production
age = int(input("Enter your age: "))

color = input("Enter your favorite color: ")

# Calculate year of birth (assumes birthday already passed this year)
year_of_birth = date.today().year - age

print(f"Hello, {name}! You were born in {year_of_birth}. Your favorite color is {color}.")

# Accept weight as float and convert to pounds
weight_kg = float(input("Enter your weight in kilograms (e.g. 70.5): "))
KG_TO_LB = 2.20462  # Conversion constant
weight_lb = weight_kg * KG_TO_LB
# Format: .1f = 1 decimal place, .2f = 2 decimal places
print(f"Thanks, {name}! Your weight is {weight_kg:.1f} kg (~{weight_lb:.2f} lb).")

# Use double quotes to avoid escaping apostrophes
print("Python's class goes fine!")
# Using single quotes requires escaping apostrophes but allows unescaped double quotes
print('Python\'s class "goes" fine!')

# Triple-quoted strings preserve newlines for multi-line messages
message = f'''Hi {name},

This is the founder of the unicorn company who wants to talk to you. Please
connect with me as soon as possible.

Thank you
'''
print(message)

# ----------------------------
# STRING CONCATENATION EXAMPLES
# ----------------------------

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

print(f"\n--- len() Function ---")
test_string = "Python"
print(f"len('{test_string}') = {len(test_string)}")

# len() counts all characters including spaces and punctuation
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

# ==============================================================================================
# STRING INDEXING & SLICING - COMPREHENSIVE GUIDE
# ==============================================================================================
print(f"\n--- STRING INDEXING & SLICING ---")

course = "Python Learning"
print(f"String: '{course}'")
print(f"Indices: {' '.join(str(i) for i in range(len(course)))}")
print(f"Characters: {' '.join(course)}")

# IMPORTANT: Python indexing is 0-based, meaning the first character is at index 0

# SINGLE CHARACTER ACCESS (Indexing)
print("\n1. SINGLE CHARACTER ACCESS (Indexing):")
print(f"  course[0] = '{course[0]}'   # First character")
print(f"  course[1] = '{course[1]}'   # Second character")
print(f"  course[4] = '{course[4]}'   # Fifth character (P-y-t-h-o)")
print(f"  course[-1] = '{course[-1]}'  # Last character (negative index)")
print(f"  course[-2] = '{course[-2]}'  # Second-to-last character")

# SLICING BASICS - Syntax: string[START:STOP:STEP]
print("\n2. BASIC SLICING (syntax: [START:STOP:STEP]):")
print(f"  IMPORTANT: STOP is EXCLUSIVE (not included in the slice)")

print("\n  2a. START:STOP (common case, step=1 by default):")
print(f"    course[0:6] = '{course[0:6]}'    # Characters at indices 0,1,2,3,4,5 (NOT 6)")
print(f"    course[7:15] = '{course[7:15]}'  # From index 7 to 14 (spaces not included)")

print("\n  2b. :STOP (start defaults to 0):")
print(f"    course[:6] = '{course[:6]}'      # Same as course[0:6]")
print(f"    course[:1] = '{course[:1]}'      # Just the first character")
print(f"    course[:0] = '{course[:0]}'      # Empty string (stops before index 0)")

print("\n  2c. START: (stop defaults to end of string):")
print(f"    course[7:] = '{course[7:]}'      # From index 7 to the end")
print(f"    course[0:] = '{course[0:]}'      # Entire string (from start to end)")

print("\n  2d. Negative indices (count backwards from end):")
print(f"    course[-8:] = '{course[-8:]}'    # Last 8 characters")
print(f"    course[:-7] = '{course[:-7]}'    # Everything except the last 7 characters")
print(f"    course[-6:-1] = '{course[-6:-1]}'  # Characters from -6 to -1 (excludes last)")

print("\n3. SLICING WITH STEP (syntax: [START:STOP:STEP]):")
print(f"  course[::2] = '{course[::2]}'      # Every 2nd character (start:stop defaults, step=2)")
print(f"  course[::3] = '{course[::3]}'      # Every 3rd character")
print(f"  course[1::2] = '{course[1::2]}'    # Every 2nd char starting from index 1")

print("\n4. STEP = -1 (REVERSING):")
print(f"  course[::-1] = '{course[::-1]}'    # Reverse entire string")
print(f"  course[10:2:-1] = '{course[10:2:-1]}'  # Reverse from index 10 down to (but not including) 2")

print("\n5. STEP = -2 (REVERSE, every 2nd character):")
print(f"  course[::-2] = '{course[::-2]}'    # Reverse, every 2nd character")

print("\n6. EDGE CASES (slicing is safe—no errors on out-of-bounds):")
print(f"  course[5:5] = '{course[5:5]}'      # Empty (start == stop)")
print(f"  course[10:5] = '{course[10:5]}'    # Empty (stop < start with positive step)")
print(f"  course[100:110] = '{course[100:110]}'  # Empty (out of bounds—no error!)")
print(f"  course[-100:5] = '{course[-100:5]}'  # Starts from beginning (negative OOB)")
print(f"  course[5:len(course)] = '{course[5:len(course)]}'  # From index 5 to end (using len())")

print("\n7. BONUS: SLICING WITH LISTS (same rules apply):")
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"  list: {my_list}")
print(f"  list[1:4] = {my_list[1:4]}      # Indices 1, 2, 3")
print(f"  list[-3:] = {my_list[-3:]}      # Last 3 elements")
print(f"  list[::2] = {my_list[::2]}      # Every 2nd element")
print(f"  list[::-1] = {my_list[::-1]}    # Reversed")

# Inspect variable types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of weight_kg:", type(weight_kg))
print("Type of weight_lb:", type(weight_lb))
print("Type of course:", type(course))

# ==============================================================================================
# STRING METHODS & FUNCTIONS - COMPREHENSIVE GUIDE
# ==============================================================================================
print("\n" + "="*80)
print("STRING METHODS & FUNCTIONS")
print("="*80)

test_str = "Hello World"
test_str2 = "  Python Programming  "
test_str3 = "Hello,Python,World"

# 1. CASE CONVERSION METHODS
print("\n1. CASE CONVERSION METHODS:")
print(f"   Original: '{test_str}'")
print(f"   .upper(): '{test_str.upper()}'")
print(f"   .lower(): '{test_str.lower()}'")
print(f"   .capitalize(): '{test_str.capitalize()}'  # First char uppercase, rest lowercase")
print(f"   .title(): '{test_str.title()}'  # Capitalize first letter of each word")
print(f"   .swapcase(): '{test_str.swapcase()}'  # Toggle case of each character")

# 2. WHITESPACE METHODS
print("\n2. WHITESPACE/TRIMMING METHODS:")
print(f"   Original: '{test_str2}' (with spaces)")
print(f"   .strip(): '{test_str2.strip()}'  # Remove leading/trailing whitespace")
print(f"   .lstrip(): '{test_str2.lstrip()}'  # Remove leading whitespace only")
print(f"   .rstrip(): '{test_str2.rstrip()}'  # Remove trailing whitespace only")

# 3. STRING SEARCH METHODS (returns index or -1)
print("\n3. STRING SEARCH METHODS:")
search_str = "Hello World, Hello Python"
print(f"   String: '{search_str}'")
print(f"   .find('Hello'): {search_str.find('Hello')}  # First occurrence (0-based index)")
print(f"   .find('World'): {search_str.find('World')}")
print(f"   .find('Ruby'): {search_str.find('Ruby')}  # Returns -1 if not found")
print(f"   .rfind('Hello'): {search_str.rfind('Hello')}  # Last occurrence from right")
print(f"   .index('World'): {search_str.index('World')}  # Like find() but raises error if not found")

# 4. STRING COUNT METHOD
print("\n4. STRING COUNT METHOD:")
count_str = "banana"
print(f"   String: '{count_str}'")
print(f"   .count('a'): {count_str.count('a')}  # Count occurrences of substring")
print(f"   .count('an'): {count_str.count('an')}")
print(f"   .count('x'): {count_str.count('x')}  # Returns 0 if not found")

# 5. STRING START/END CHECKING
print("\n5. START/END CHECKING METHODS (return True/False):")
filename = "document.pdf"
print(f"   String: '{filename}'")
print(f"   .startswith('doc'): {filename.startswith('doc')}")
print(f"   .startswith('file'): {filename.startswith('file')}")
print(f"   .endswith('.pdf'): {filename.endswith('.pdf')}")
print(f"   .endswith('.txt'): {filename.endswith('.txt')}")

# 6. STRING REPLACEMENT METHOD
print("\n6. STRING REPLACEMENT METHOD:")
replace_str = "I like cats, cats are cute"
print(f"   Original: '{replace_str}'")
print(f"   .replace('cats', 'dogs'): '{replace_str.replace('cats', 'dogs')}'")
print(f"   .replace('cats', 'dogs', 1): '{replace_str.replace('cats', 'dogs', 1)}'  # Only 1st occurrence")

# 7. STRING SPLIT METHOD (returns list)
print("\n7. STRING SPLIT METHOD (returns list):")
print(f"   String: '{test_str3}'")
print(f"   .split(','): {test_str3.split(',')}  # Split by delimiter")
split_by_space = "Python is awesome"
print(f"   String: '{split_by_space}'")
print(f"   .split(): {split_by_space.split()}  # Split by whitespace (default)")

# 8. STRING JOIN METHOD (opposite of split)
print("\n8. STRING JOIN METHOD (opposite of split):")
words_list = ['Hello', 'Python', 'World']
print(f"   List: {words_list}")
print(f"   ' '.join(list): '{' '.join(words_list)}'  # Join with space")
print(f"   '-'.join(list): '{'-'.join(words_list)}'  # Join with hyphen")
print(f"   ''.join(list): '{' '.join(words_list)}'  # Join with nothing")

# 9. CHARACTER TYPE CHECKING METHODS (return True/False)
print("\n9. CHARACTER TYPE CHECKING METHODS (return True/False):")
str1 = "12345"
str2 = "Hello"
str3 = "123abc"
str4 = "   "
print(f"   '{str1}'.isdigit(): {str1.isdigit()}  # All digits?")
print(f"   '{str2}'.isalpha(): {str2.isalpha()}  # All alphabetic characters?")
print(f"   '{str3}'.isalnum(): {str3.isalnum()}  # All alphanumeric (letters + digits)?")
print(f"   '{str4}'.isspace(): {str4.isspace()}  # All whitespace?")
print(f"   '{str2}'.isupper(): {str2.isupper()}  # All uppercase?")
print(f"   '{str2}'.islower(): {str2.islower()}  # All lowercase?")
print(f"   '{test_str.upper()}'.isupper(): {test_str.upper().isupper()}")

# 10. STRING PADDING/ALIGNMENT METHODS
print("\n10. STRING PADDING/ALIGNMENT METHODS:")
pad_str = "Python"
print(f"   Original: '{pad_str}'")
print(f"   .center(15): '{pad_str.center(15)}'  # Center in field of 15 chars")
print(f"   .center(15, '*'): '{pad_str.center(15, '*')}'  # Center with * as padding")
print(f"   .ljust(15): '{pad_str.ljust(15)}'  # Left justify in 15 chars")
print(f"   .rjust(15): '{pad_str.rjust(15)}'  # Right justify in 15 chars")
print(f"   .zfill(10): '{pad_str.zfill(10)}'  # Pad with zeros (useful for numbers)")
zip_code = "12345"
print(f"   .zfill(10) for '12345': '{zip_code.zfill(10)}'")

# 11. PRACTICAL EXAMPLES: COMBINING METHODS
print("\n11. PRACTICAL EXAMPLES (Combining multiple methods):")
user_input = "  john doe  "
print(f"   Original input: '{user_input}'")
processed = user_input.strip().title()
print(f"   .strip().title(): '{processed}'  # Clean and format name")

email = "  USER@EXAMPLE.COM  "
normalized = email.strip().lower()
print(f"   Email input: '{email}'")
print(f"   .strip().lower(): '{normalized}'  # Normalize email")

path = "C:\\Users\\John\\documents\\file.pdf"
print(f"   File path: '{path}'")
print(f"   .split('\\\\'): {path.split(chr(92))}")  # Split by backslash (need chr(92) for display)

# 12. BONUS: USEFUL STRING FUNCTIONS
print("\n12. BUILT-IN STRING FUNCTIONS (not methods):")
string_for_reverse = "Python"
print(f"   Original: '{string_for_reverse}'")
print(f"   len(string): {len(string_for_reverse)}")
print(f"   reversed(string) as list: {list(reversed(string_for_reverse))}")
print(f"   max(string): '{max(string_for_reverse)}'  # Max character (by ASCII value)")
print(f"   min(string): '{min(string_for_reverse)}'  # Min character (by ASCII value)")
print(f"   sorted(string): {sorted(string_for_reverse)}")
print(f"   'h' in 'Hello': {'h' in 'Hello'}")
print(f"   'x' not in 'Hello': {'x' not in 'Hello'}")

# ----------------------------
# OPERATOR EXAMPLES
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

# Combine relational and logical operators
print("\nCombined expressions:")
age_check = age >= 18
print(f"age >= 18 and weight_kg > 50: {age_check and weight_kg > 50}")
print(f"(age < 30) or (weight_kg < 60): {(age < 30) or (weight_kg < 60)}")

# ==============================================================================================
# CONDITIONAL STATEMENTS - COMPREHENSIVE GUIDE
# ==============================================================================================
print("\n" + "="*80)
print("CONDITIONAL STATEMENTS (if/elif/else)")
print("="*80)

# 1. SIMPLE IF STATEMENT
print("\n1. SIMPLE IF STATEMENT:")
print("   Syntax: if condition:")
print("       statement(s)")
number = 10
if number > 5:
    print(f"   '{number}' is greater than 5")

# 2. IF-ELSE STATEMENT
print("\n2. IF-ELSE STATEMENT:")
print("   Syntax: if condition:")
print("       statement(s)")
print("   else:")
print("       statement(s)")
temperature = 15
if temperature > 20:
    print(f"   Temperature {temperature}°C is warm")
else:
    print(f"   Temperature {temperature}°C is cold")

# 3. IF-ELIF-ELSE STATEMENT (multiple conditions)
print("\n3. IF-ELIF-ELSE STATEMENT (multiple conditions):")
print("   Syntax: if condition1:")
print("       statement(s)")
print("   elif condition2:")
print("       statement(s)")
print("   else:")
print("       statement(s)")
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"   Score {score} -> Grade: {grade}")

# 4. NESTED IF STATEMENTS
print("\n4. NESTED IF STATEMENTS:")
print("   Conditions inside conditions")
user_age = age
is_citizen = True
if user_age >= 18:
    if is_citizen:
        print(f"   {name} is eligible to vote")
    else:
        print(f"   {name} is not eligible to vote (not a citizen)")
else:
    print(f"   {name} is too young to vote")

# 5. COMBINING CONDITIONS WITH LOGICAL OPERATORS
print("\n5. COMBINING CONDITIONS WITH LOGICAL OPERATORS:")
print("   Using 'and', 'or', 'not'")

# Using 'and'
print("\n   a) Using 'and' (both conditions must be True):")
user_age = age
income = 50000
if user_age >= 21 and income > 30000:
    print(f"   {name} qualifies for the loan (age >= 21 AND income > $30,000)")
else:
    print(f"   {name} does NOT qualify for the loan")

# Using 'or'
print("\n   b) Using 'or' (at least one condition must be True):")
is_student = False
is_senior = user_age >= 65
if is_student or is_senior:
    print(f"   {name} gets a discount (student OR senior)")
else:
    print(f"   {name} does NOT get a discount")

# Using 'not'
print("\n   c) Using 'not' (negates condition):")
is_raining = False
if not is_raining:
    print(f"   Let's go outside (NOT raining)")
else:
    print(f"   Let's stay inside (it's raining)")

# 6. PRACTICAL EXAMPLE: CATEGORY CLASSIFICATION
print("\n6. PRACTICAL EXAMPLE: CLASSIFY AGE GROUPS")
person_age = user_age
if person_age < 13:
    category = "Child"
elif person_age < 20:
    category = "Teenager"
elif person_age < 65:
    category = "Adult"
else:
    category = "Senior"
print(f"   {name} (age {person_age}) is classified as: {category}")

# 7. PRACTICAL EXAMPLE: VALIDATION
print("\n7. PRACTICAL EXAMPLE: INPUT VALIDATION")
user_password = "SecurePass123"
password_valid = True

if len(user_password) < 8:
    password_valid = False
    print("   ✗ Password is too short (minimum 8 characters)")
elif not any(char.isdigit() for char in user_password):
    password_valid = False
    print("   ✗ Password must contain at least one digit")
elif not any(char.isupper() for char in user_password):
    password_valid = False
    print("   ✗ Password must contain at least one uppercase letter")
elif not any(char.islower() for char in user_password):
    password_valid = False
    print("   ✗ Password must contain at least one lowercase letter")
else:
    print(f"   ✓ Password '{user_password}' is valid!")

# 8. PRACTICAL EXAMPLE: WEATHER RECOMMENDATION
print("\n8. PRACTICAL EXAMPLE: WEATHER-BASED RECOMMENDATION")
current_temp = temperature
if current_temp < 0:
    recommendation = "Wear heavy winter coat and boots"
elif current_temp < 10:
    recommendation = "Wear jacket and warm clothes"
elif current_temp < 20:
    recommendation = "Wear light layers"
elif current_temp < 30:
    recommendation = "Wear t-shirt and shorts"
else:
    recommendation = "Wear sunscreen and light clothing"
print(f"   Temperature {current_temp}°C -> {recommendation}")

# 9. PRACTICAL EXAMPLE: DISCOUNT CALCULATOR
print("\n9. PRACTICAL EXAMPLE: DISCOUNT CALCULATOR")
purchase_amount = 150
if purchase_amount >= 200:
    discount = 0.20  # 20% discount
elif purchase_amount >= 100:
    discount = 0.10  # 10% discount
elif purchase_amount >= 50:
    discount = 0.05  # 5% discount
else:
    discount = 0  # No discount
final_price = purchase_amount * (1 - discount)
print(f"   Purchase: ${purchase_amount:.2f}")
print(f"   Discount: {discount*100:.0f}%")
print(f"   Final Price: ${final_price:.2f}")

# 10. COMPARISON: ONE-LINER TERNARY CONDITIONAL
print("\n10. ONE-LINER TERNARY CONDITIONAL (Conditional Expression):")
print("   Syntax: value_if_true if condition else value_if_false")
age_category = "Adult" if user_age >= 18 else "Minor"
print(f"   {name} is a {age_category} (using ternary expression)")

# Ternary with multiple conditions
status = "Pass" if score >= 60 else "Fail"
print(f"   Score {score} -> {status}")

# Nested ternary (not recommended for readability)
priority = "High" if score >= 90 else ("Medium" if score >= 70 else "Low")
print(f"   Score {score} -> Priority: {priority}")

# ==============================================================================================
# GREATEST AMONG 3 NUMBERS - COMPREHENSIVE GUIDE
# ==============================================================================================
print("\n" + "="*80)
print("GREATEST AMONG 3 NUMBERS")
print("="*80)

# METHOD 1: Using if-elif-else statements
print("\n1. METHOD 1: Using if-elif-else statements")
print("   Input 3 numbers and find the greatest using conditional logic")

num1 = 15
num2 = 42
num3 = 28

print(f"   num1 = {num1}, num2 = {num2}, num3 = {num3}")

if num1 >= num2 and num1 >= num3:
    greatest = num1
    print(f"   → Greatest: {greatest} (num1)")
elif num2 >= num3:
    greatest = num2
    print(f"   → Greatest: {greatest} (num2)")
else:
    greatest = num3
    print(f"   → Greatest: {greatest} (num3)")

# METHOD 2: Using nested if-else
print("\n2. METHOD 2: Using nested if-else statements")
print("   Simpler approach: compare first two, then compare with third")

num1 = 15
num2 = 42
num3 = 28

print(f"   num1 = {num1}, num2 = {num2}, num3 = {num3}")

if num1 > num2:
    if num1 > num3:
        greatest = num1
    else:
        greatest = num3
else:
    if num2 > num3:
        greatest = num2
    else:
        greatest = num3

print(f"   → Greatest: {greatest}")

# METHOD 3: Using built-in max() function (RECOMMENDED)
print("\n3. METHOD 3: Using built-in max() function (RECOMMENDED)")
print("   Most Pythonic and elegant approach")

num1 = 15
num2 = 42
num3 = 28

print(f"   num1 = {num1}, num2 = {num2}, num3 = {num3}")
greatest = max(num1, num2, num3)
print(f"   greatest = max({num1}, {num2}, {num3})")
print(f"   → Greatest: {greatest}")

# METHOD 4: Using ternary conditional expressions
print("\n4. METHOD 4: Using ternary conditional expressions (one-liner)")

num1 = 15
num2 = 42
num3 = 28

print(f"   num1 = {num1}, num2 = {num2}, num3 = {num3}")
greatest = num1 if (num1 >= num2 and num1 >= num3) else (num2 if num2 >= num3 else num3)
print(f"   → Greatest: {greatest}")

# METHOD 5: Function to find greatest among 3 numbers
print("\n5. METHOD 5: Creating a reusable function")

def find_greatest(a, b, c):
    """
    Find and return the greatest among three numbers.
    
    Args:
        a, b, c: Three numbers to compare
    
    Returns:
        The greatest of the three numbers
    """
    return max(a, b, c)

num1 = 15
num2 = 42
num3 = 28

print(f"   num1 = {num1}, num2 = {num2}, num3 = {num3}")
result = find_greatest(num1, num2, num3)
print(f"   find_greatest({num1}, {num2}, {num3}) = {result}")
print(f"   → Greatest: {result}")

# Test with different numbers
test_cases = [
    (10, 20, 30),
    (100, 50, 75),
    (5, 5, 5),
    (-10, -20, -5),
    (0, -5, 10)
]

print("\n   Testing with various inputs:")
for a, b, c in test_cases:
    result = find_greatest(a, b, c)
    print(f"   find_greatest({a:4d}, {b:4d}, {c:4d}) = {result:4d}")

# METHOD 6: Interactive function with user input
print("\n6. METHOD 6: Interactive function with user input")
print("   (This would ask for user input in interactive mode)")

def greatest_interactive():
    """
    Interactive function to find greatest among 3 user-provided numbers.
    """
    print("\n   Enter three numbers:")
    try:
        x = float(input("   Enter first number: "))
        y = float(input("   Enter second number: "))
        z = float(input("   Enter third number: "))
        
        greatest = max(x, y, z)
        print(f"\n   Numbers: {x}, {y}, {z}")
        print(f"   → Greatest: {greatest}")
        return greatest
    except ValueError:
        print("   Error: Please enter valid numbers!")
        return None

# Commented out to avoid blocking execution
# greatest_interactive()

print("   (Function defined but not called to avoid blocking)")

# METHOD 7: Using list and max()
print("\n7. METHOD 7: Using list and max() function")

numbers = [15, 42, 28]
print(f"   numbers = {numbers}")
greatest = max(numbers)
print(f"   greatest = max(numbers)")
print(f"   → Greatest: {greatest}")

# METHOD 8: Function with multiple return values
print("\n8. METHOD 8: Return greatest and its position")

def greatest_with_position(a, b, c):
    """
    Find greatest and return it along with its position.
    
    Returns:
        Tuple: (greatest_value, position: 1, 2, or 3)
    """
    numbers = [a, b, c]
    greatest = max(numbers)
    position = numbers.index(greatest) + 1
    return greatest, position

num1 = 15
num2 = 42
num3 = 28

print(f"   num1 = {num1}, num2 = {num2}, num3 = {num3}")
value, pos = greatest_with_position(num1, num2, num3)
print(f"   greatest = {value}, position = num{pos}")
print(f"   → Greatest: {value} (at position {pos})")

print("\n" + "="*80)
print("LISTS & TUPLES - COMPREHENSIVE GUIDE")
print("="*80)

# ==============================================================================================
# LISTS - ORDERED, MUTABLE (changeable), INDEXED
# ==============================================================================================

print("\n" + "-"*80)
print("PART 1: LISTS - ORDERED, MUTABLE (changeable), INDEXED")
print("-"*80)

# 1. CREATING LISTS
print("\n1. CREATING LISTS:")
print("   # Empty list")
empty_list = []
print(f"   empty_list = []")
print(f"   Output: {empty_list}")

print("\n   # List with numbers")
numbers = [10, 20, 30, 40, 50]
print(f"   numbers = [10, 20, 30, 40, 50]")
print(f"   Output: {numbers}")

print("\n   # List with mixed data types")
mixed_list = [1, "Python", 3.14, True, None]
print(f"   mixed_list = [1, 'Python', 3.14, True, None]")
print(f"   Output: {mixed_list}")

print("\n   # List with strings")
fruits = ["apple", "banana", "cherry", "date"]
print(f"   fruits = ['apple', 'banana', 'cherry', 'date']")
print(f"   Output: {fruits}")

# 2. ACCESSING ELEMENTS (Indexing)
print("\n2. ACCESSING ELEMENTS (Indexing):")
print(f"   numbers = {numbers}")
print(f"   numbers[0] = {numbers[0]}      # First element (index 0)")
print(f"   numbers[2] = {numbers[2]}      # Third element (index 2)")
print(f"   numbers[-1] = {numbers[-1]}    # Last element (negative index)")
print(f"   numbers[-2] = {numbers[-2]}    # Second-to-last element")

# 3. SLICING LISTS
print("\n3. SLICING LISTS (syntax: list[START:STOP:STEP]):")
print(f"   numbers = {numbers}")
print(f"   numbers[1:4] = {numbers[1:4]}   # Elements at indices 1, 2, 3 (4 excluded)")
print(f"   numbers[2:] = {numbers[2:]}     # From index 2 to end")
print(f"   numbers[:3] = {numbers[:3]}     # From start to index 3 (excluded)")
print(f"   numbers[::2] = {numbers[::2]}   # Every 2nd element")
print(f"   numbers[::-1] = {numbers[::-1]} # Reversed list")

# 4. LIST LENGTH
print("\n4. LIST LENGTH (len() function):")
print(f"   len(numbers) = {len(numbers)}")
print(f"   len(fruits) = {len(fruits)}")
print(f"   len(empty_list) = {len(empty_list)}")

# 5. MODIFYING LISTS (Mutable - changeable)
print("\n5. MODIFYING LISTS (Mutable - changeable):")

# 5a. Adding elements
print("\n   5a. ADDING ELEMENTS:")
fruits_copy = fruits.copy()  # Copy to avoid modifying original
print(f"   Original: {fruits_copy}")

fruits_copy.append("elderberry")  # Add to end
print(f"   After .append('elderberry'): {fruits_copy}")

fruits_copy.insert(1, "blueberry")  # Insert at specific index
print(f"   After .insert(1, 'blueberry'): {fruits_copy}")

fruits_copy.extend(["fig", "grape"])  # Add multiple elements
print(f"   After .extend(['fig', 'grape']): {fruits_copy}")

# 5b. Removing elements
print("\n   5b. REMOVING ELEMENTS:")
print(f"   Current list: {fruits_copy}")

fruits_copy.remove("blueberry")  # Will raise error if not found, let's use blueberry
print(f"   After .remove('blueberry'): {[x for x in fruits_copy if x != 'blueberry']}")

popped = fruits_copy.pop()  # Remove last element and return it
print(f"   After .pop() (removed: {popped}): {fruits_copy}")

popped_index = fruits_copy.pop(0)  # Remove element at index 0
print(f"   After .pop(0) (removed: {popped_index}): {fruits_copy}")

# 5c. Replacing elements
print("\n   5c. REPLACING ELEMENTS:")
numbers_copy = numbers.copy()
print(f"   Original: {numbers_copy}")
numbers_copy[1] = 999
print(f"   After numbers_copy[1] = 999: {numbers_copy}")

numbers_copy[2:4] = [111, 222]  # Replace slice
print(f"   After numbers_copy[2:4] = [111, 222]: {numbers_copy}")

# 5d. Clearing a list
print("\n   5d. CLEARING A LIST:")
temp_list = [1, 2, 3, 4, 5]
print(f"   Before clear: {temp_list}")
temp_list.clear()
print(f"   After .clear(): {temp_list}")

# 6. LIST METHODS & OPERATIONS
print("\n6. LIST METHODS & OPERATIONS:")
numbers = [10, 20, 30, 40, 50]
print(f"   numbers = {numbers}")

print(f"\n   .count(value) - Count occurrences:")
counts_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"   {counts_list}.count(3) = {counts_list.count(3)}")

print(f"\n   .index(value) - Find first index of value:")
print(f"   {fruits}.index('cherry') = {fruits.index('cherry')}")

print(f"\n   .sort() - Sort in place (modifies original):")
unsorted = [50, 10, 30, 20, 40]
print(f"   unsorted = {unsorted}")
unsorted.sort()
print(f"   After .sort(): {unsorted}")

unsorted.sort(reverse=True)
print(f"   After .sort(reverse=True): {unsorted}")

print(f"\n   sorted() - Return sorted copy (doesn't modify):")
unsorted = [50, 10, 30, 20, 40]
sorted_list = sorted(unsorted)
print(f"   Original: {unsorted}")
print(f"   sorted(unsorted) = {sorted_list}")

print(f"\n   .reverse() - Reverse in place:")
rev_list = [1, 2, 3, 4, 5]
print(f"   Before: {rev_list}")
rev_list.reverse()
print(f"   After .reverse(): {rev_list}")

print(f"\n   min() and max() - Find minimum/maximum:")
nums = [15, 3, 42, 7, 23]
print(f"   {nums}")
print(f"   min(nums) = {min(nums)}")
print(f"   max(nums) = {max(nums)}")

print(f"\n   sum() - Sum all elements:")
print(f"   sum({nums}) = {sum(nums)}")

# 7. ITERATING THROUGH LISTS
print("\n7. ITERATING THROUGH LISTS:")
print(f"   fruits = {fruits}")

print("\n   Method 1: for-in loop")
for fruit in fruits:
    print(f"      - {fruit}")

print("\n   Method 2: for-in with index using enumerate()")
for i, fruit in enumerate(fruits):
    print(f"      [{i}] = {fruit}")

print("\n   Method 3: for loop with range()")
for i in range(len(fruits)):
    print(f"      [{i}] = {fruits[i]}")

# ==============================================================================================
# TUPLES - ORDERED, IMMUTABLE (unchangeable), INDEXED
# ==============================================================================================

print("\n" + "-"*80)
print("PART 2: TUPLES - ORDERED, IMMUTABLE (unchangeable), INDEXED")
print("-"*80)

# 1. CREATING TUPLES
print("\n1. CREATING TUPLES:")

print("\n   # Empty tuple")
empty_tuple = ()
print(f"   empty_tuple = ()")
print(f"   Output: {empty_tuple}")

print("\n   # Tuple with numbers")
coord = (10, 20, 30)
print(f"   coord = (10, 20, 30)")
print(f"   Output: {coord}")

print("\n   # Tuple with mixed data types")
mixed_tuple = (1, "Python", 3.14, True, None)
print(f"   mixed_tuple = (1, 'Python', 3.14, True, None)")
print(f"   Output: {mixed_tuple}")

print("\n   # Single-element tuple (IMPORTANT: needs trailing comma)")
single = (42,)
print(f"   single = (42,)  # Note: trailing comma makes it a tuple")
print(f"   Output: {single}")
print(f"   Without comma: (42) = {42} (just a number, not a tuple)")

print("\n   # Tuple without parentheses (implicit)")
implicit_tuple = 1, 2, 3
print(f"   implicit_tuple = 1, 2, 3  # Parentheses are optional")
print(f"   Output: {implicit_tuple}")

# 2. ACCESSING TUPLE ELEMENTS
print("\n2. ACCESSING TUPLE ELEMENTS:")
print(f"   coord = {coord}")
print(f"   coord[0] = {coord[0]}      # First element")
print(f"   coord[1] = {coord[1]}      # Second element")
print(f"   coord[-1] = {coord[-1]}    # Last element")

# 3. SLICING TUPLES
print("\n3. SLICING TUPLES (same as lists):")
numbers_tuple = (10, 20, 30, 40, 50)
print(f"   numbers_tuple = {numbers_tuple}")
print(f"   numbers_tuple[1:4] = {numbers_tuple[1:4]}")
print(f"   numbers_tuple[::2] = {numbers_tuple[::2]}")
print(f"   numbers_tuple[::-1] = {numbers_tuple[::-1]}")

# 4. TUPLE LENGTH
print("\n4. TUPLE LENGTH:")
print(f"   len(coord) = {len(coord)}")
print(f"   len(numbers_tuple) = {len(numbers_tuple)}")

# 5. WHY TUPLES ARE IMMUTABLE (UNCHANGEABLE)
print("\n5. TUPLES ARE IMMUTABLE (UNCHANGEABLE):")
print(f"   coord = {coord}")
print(f"   Trying to change: coord[0] = 999")
try:
    coord[0] = 999
except TypeError as e:
    print(f"   Error: {e}")
    print(f"   → Tuples cannot be modified after creation!")

# 6. TUPLE METHODS & OPERATIONS
print("\n6. TUPLE METHODS & OPERATIONS:")

colors = ("red", "green", "blue", "red", "yellow")
print(f"   colors = {colors}")

print(f"\n   .count(value) - Count occurrences:")
print(f"   colors.count('red') = {colors.count('red')}")

print(f"\n   .index(value) - Find first index of value:")
print(f"   colors.index('blue') = {colors.index('blue')}")

print(f"\n   len() - Tuple length:")
print(f"   len(colors) = {len(colors)}")

print(f"\n   min() and max():")
nums_tuple = (15, 3, 42, 7, 23)
print(f"   {nums_tuple}")
print(f"   min(nums_tuple) = {min(nums_tuple)}")
print(f"   max(nums_tuple) = {max(nums_tuple)}")

print(f"\n   sum():")
print(f"   sum({nums_tuple}) = {sum(nums_tuple)}")

# 7. ITERATING THROUGH TUPLES
print("\n7. ITERATING THROUGH TUPLES:")
print(f"   colors = {colors}")

print("\n   Using for-in loop:")
for color in colors:
    print(f"      - {color}")

print("\n   Using enumerate():")
for i, color in enumerate(colors):
    print(f"      [{i}] = {color}")

# 8. TUPLE UNPACKING
print("\n8. TUPLE UNPACKING:")

point = (10, 20, 30)
x, y, z = point
print(f"   point = {point}")
print(f"   x, y, z = point")
print(f"   x = {x}, y = {y}, z = {z}")

print("\n   Swapping variables with tuple unpacking:")
a, b = 5, 10
print(f"   Before: a = {a}, b = {b}")
a, b = b, a  # Clever Python trick!
print(f"   After:  a = {a}, b = {b}")

# ==============================================================================================
# LISTS vs TUPLES - COMPARISON
# ==============================================================================================

print("\n" + "-"*80)
print("LISTS vs TUPLES - SIDE-BY-SIDE COMPARISON")
print("-"*80)

print("\n╔════════════════════╦══════════════════════╦══════════════════════╗")
print("║ FEATURE            ║ LIST                 ║ TUPLE                ║")
print("╠════════════════════╬══════════════════════╬══════════════════════╣")
print("║ Syntax             ║ [1, 2, 3]            ║ (1, 2, 3)            ║")
print("║ Mutable            ║ YES (changeable)     ║ NO (unchangeable)    ║")
print("║ Speed              ║ Slower               ║ Faster               ║")
print("║ Memory             ║ More                 ║ Less                 ║")
print("║ Indexing           ║ Yes - [i]            ║ Yes - [i]            ║")
print("║ Slicing            ║ Yes                  ║ Yes                  ║")
print("║ Methods            ║ append, remove, etc. ║ count, index only    ║")
print("║ Dict Key           ║ NO (unhashable)      ║ YES (hashable)       ║")
print("║ Use Case           ║ Collections change   ║ Fixed collections    ║")
print("╚════════════════════╩══════════════════════╩══════════════════════╝")

print("\nCommon Methods Comparison:")
print("   LIST methods: append, extend, insert, remove, pop, clear, sort, reverse")
print("   TUPLE methods: count, index")

# 9. PRACTICAL EXAMPLES
print("\n" + "-"*80)
print("PRACTICAL EXAMPLES")
print("-"*80)

print("\n1. USING TUPLE FOR COORDINATES (immutable, won't change):")
coordinates = [
    (0, 0),
    (10, 20),
    (30, 40),
    (50, 60)
]
print(f"   coordinates = {coordinates}")
for i, (x, y) in enumerate(coordinates):
    print(f"      Point {i}: x={x}, y={y}")

print("\n2. USING LIST FOR SHOPPING CART (mutable, can change):")
cart = ["apple", "banana"]
print(f"   Initial cart: {cart}")
cart.append("orange")
print(f"   After adding orange: {cart}")
cart.remove("banana")
print(f"   After removing banana: {cart}")

print("\n3. RETURNING MULTIPLE VALUES USING TUPLE:")
def get_user_info():
    """Return user information as a tuple"""
    return ("John", "Doe", 25, "john@example.com")

name, last_name, age, email = get_user_info()
print(f"   Result: name={name}, last_name={last_name}, age={age}, email={email}")

print("\n4. USING TUPLE AS DICTIONARY KEY (list cannot be used):")
location_dict = {
    (0, 0): "Origin",
    (10, 20): "North",
    (30, 40): "South",
    (-5, -10): "West"
}
print(f"   location_dict = {{")
for key, value in location_dict.items():
    print(f"      {key}: '{value}',")
print(f"   }}")

print("\n5. FINDING SPECIFIC ITEMS IN LISTS:")
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(f"   students = {students}")
if "Charlie" in students:
    index = students.index("Charlie")
    print(f"   'Charlie' found at index {index}")

print("\n" + "="*80)

print("DICTIONARIES - COMPREHENSIVE GUIDE")

info = {
    "key" : "value",
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "scores": [85, 90, 92],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345"
    }
}   

print(f"   info = {info}")