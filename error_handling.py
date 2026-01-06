import time

# Simple comparison between two numbers
x = 10
y = 12
if y > x :
    print("y is greater than x")
if x < y :
    print(str(x) + " is less than " + str(y))

# Handling division by zero error
b = 0
# print(x / b) # This will raise a ZeroDivisionError
try:
    result = x / b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handling index out of range error
my_list = [1, 2, 3]
#print(my_list[5]) # This will raise an IndexError
try:
    print(my_list[5])
except IndexError:
    print("Error: List index out of range.")

# Handling file not found error
# with open('non_existent_file.txt', 'r') as file: # This will raise a FileNotFoundError
#     content = file.read()
#     print(content)
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")

# Handling value error during type conversion
num_str = "abc"
# num = int(num_str) # This will raise a ValueError
try:
    num = int(num_str)
    print(num)
except ValueError:
    print("Error: Cannot convert string to integer.")

# Handling keyboard interrupt (demo without hanging)
try:
    for _ in range(3):
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Process interrupted by user.")

# Handling multiple exceptions
try:
    value = my_list[5]
    result = x / b
except IndexError:
    print("Error: List index out of range.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Using finally block
try:
    result = x / 2
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

# Custom exception
class NegativeNumberError(Exception):
    pass
def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Custom Exception: {e}")

# Using else block
try:
    result = x / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Result is: {result}")

# Using assert statement
def divide(a, b):
    assert b != 0, "Denominator cannot be zero."
    return a / b
try:
    print(divide(10, 0))
except AssertionError as e:
    print(f"Assertion Error: {e}")

# Nested try-except
try:
    try:
        result = x / b
    except ZeroDivisionError:
        print("Inner Error: Division by zero is not allowed.")
    my_list[5]
except IndexError:
    print("Outer Error: List index out of range.")

# Using context manager for file operations
try:
    with open('example.txt', 'w') as file:
        file.write("Hello, World!")
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"File operation error: {e}")

# Catching all exceptions
try:
    result = x / b
    my_list[5]
except Exception as e:
    print(f"An error occurred: {e}")

# Raising exceptions manually
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
try:
    validate_age(-1)
except ValueError as e:
    print(f"Validation Error: {e}")

