### This script demonstrates various string operations in Python.
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