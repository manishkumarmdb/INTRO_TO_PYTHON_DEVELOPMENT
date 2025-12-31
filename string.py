### This script demonstrates various string operations in Python.
first_name = 'Setu'
last_Name = 'Choudhari'
print('Hello, ' + first_name + ' ' + last_Name + '!')
print('Hello, {} {}!'.format(first_name, last_Name))
### Using positional arguments in format method
print('Hello, {0} {1}!'.format(first_name, last_Name))
print('Hello, {1} {0}!'.format(first_name, last_Name))
### Using f-strings for string interpolation
print(f'Hello, {first_name} {last_Name}!')
### Storing the full greeting in a variable
full_name = f'Hello, {first_name} {last_Name}!'

#### Taking user input for first and last name
first_name = input('Enter your first name: ')
last_Name = input('Enter your last name: ')
full_name = first_name + ' ' + last_Name
print('Hello, ' + full_name)

print(f'Hello, {full_name}!')
print('Display in capitalize format:')
print(f'Hello, {full_name.capitalize()}!')

sentence = 'This is a sample sentence.'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('s'))
print(sentence.title())
print(sentence.replace('sample', 'test'))