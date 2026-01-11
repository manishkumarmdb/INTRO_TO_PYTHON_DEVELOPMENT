
# loops.py
# This script demonstrates the use of for loops in Python.
for name in ['Alice', 'Bob', 'Charlie']:
    print(f'Hello, {name}!')
# Using range() to iterate over a sequence of numbers
for i in range(5):
    print(f'Number: {i}')
# Using range() with a start and end value
for i in range(2, 7):
    print(f'Number from 2 to 6: {i}')
# Using range() with a step value
for i in range(1, 10, 2):
    print(f'Odd Number: {i}')
# Using range() with a step value
for i in range(0, 10, 2):
    print(f'Even Number: {i}')
# Nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f'i: {i}, j: {j}')
# Using else with for loop
for i in range(3):
    print(f'Iteration {i}')
else:
    print('Loop completed successfully!')
# Using break in a for loop
for i in range(5):
    if i == 3:
        print('Breaking the loop at i = 3')
        break
    print(f'Current value: {i}')
# Using continue in a for loop
for i in range(5):
    if i % 2 == 0:
        print(f'Skipping even number: {i}')
        continue
    print(f'Odd number: {i}')
# Using pass in a for loop
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    print(f'Value: {i}')
# Using enumerate() to get index and value
for index, value in enumerate(['apple', 'banana', 'cherry']):
    print(f'Index: {index}, Value: {value}')
# Using zip() to iterate over multiple sequences
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old.')
# Using list comprehension with for loop
squares = [x**2 for x in range(5)]
print(f'Squares: {squares}')
# Using dictionary comprehension with for loop
square_dict = {x: x**2 for x in range(5)}
print(f'Square Dictionary: {square_dict}')
# Using set comprehension with for loop
square_set = {x**2 for x in range(5)}
print(f'Square Set: {square_set}')
# Using generator expression with for loop
square_gen = (x**2 for x in range(5))
print('Generated Squares:' + square_gen.__str__())
for square in square_gen:
    print(f'Generated Square: {square}')

# While loop example
count = 0
while count < 5:
    print(f'Count is: {count}')
    count += 1
# Using else with while loop
count = 0
while count < 3:
    print(f'Count in while loop: {count}')
    count += 1
else:
    print('While loop completed successfully!')
# Using break in a while loop
count = 0
while count < 5:
    if count == 3:
        print('Breaking the while loop at count = 3')
        break
    print(f'Current count: {count}')
    count += 1
# Using continue in a while loop
count = 0
while count < 5:
    count += 1
    if count % 2 == 0:
        print(f'Skipping even count: {count}')
        continue
    print(f'Odd count: {count}')
# Using pass in a while loop
count = 0
while count < 5:
    if count == 2:
        pass  # Placeholder for future code
    print(f'Count value: {count}')
    count += 1
# Using nested while loops
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f'i: {i}, j: {j}')
        j += 1
    i += 1
