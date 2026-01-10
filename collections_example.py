from array import array

names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [24, 30, 22, 35]
salaries = [50000, 60000, 55000, 70000]
for i in range(len(names)):
    print(f'Name: {names[i]}, Age: {ages[i]}, Salary: {salaries[i]}')

scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
for name, score in scores.items():
    print(f'{name} scored {score} points.')
products = [{'name': 'Laptop', 'price': 999.99, 'quantity': 10},    
            {'name': 'Smartphone', 'price': 499.99, 'quantity': 25},
            {'name': 'Tablet', 'price': 299.99, 'quantity': 15}]
for product in products:
    print(f"Product: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
employees = [{'name': 'Eve', 'department': 'HR', 'salary': 60000},
                {'name': 'Frank', 'department': 'IT', 'salary': 75000},
                {'name': 'Grace', 'department': 'Finance', 'salary': 80000}]
for employee in employees:
    print(f"Employee: {employee['name']}, Department: {employee['department']}, Salary: {employee['salary']}")

# Using array module for efficient storage of numeric data
score_array = array('i', [85, 90, 78, 92])
score_array.append(88)
score_array.append(78)
for score in score_array:
    print(f'Score: {score}')

# Using array module for floating point numbers
double_array = array('d')
double_array.append(99.5)
double_array.append(87.3)
for value in double_array:
    print(f'Double value: {value}')

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
print('names size: ' + str(len(names)))  # Output: 5
names.insert(2, 'Zara')  # Insert 'Zara' at index 2
print(names)  # Output: ['Alice', 'Bob', 'Zara', 'Charlie', 'David', 'Eve']
names.remove('Bob')  # Remove 'Bob' from the list
print(names)  # Output: ['Alice', 'Zara', 'Charlie', 'David', 'Eve']
names.sort()  # Sort the list in ascending order
print(names)  # Output: ['Alice', 'Charlie', 'David', 'Eve', 'Zara']
names.reverse()  # Reverse the list
print(names)  # Output: ['Zara', 'Eve', 'David', 'Charlie', 'Alice']
popped_name = names.pop()  # Remove and return the last item
print(popped_name)  # Output: 'Alice'
print(names)  # Output: ['Zara', 'Eve', 'David', 'Charlie']

# Slicing the list
presenters = names[1:3]
print(presenters)  # Output: ['Eve', 'David']

# https://www.hackerrank.com/challenges/list-comprehensions/problem
# List Comprehensions
# x = int(input('Enter x: '))
# y = int(input('Enter y: '))
# z = int(input('Enter z: '))
# n = int(input('Enter n: '))
# result = [[i, j, k]
#     for i in range(x + 1)
#     for j in range(y + 1)
#     for k in range(z + 1)
#     if (i + j + k) != n]
# print(result)

# https://www.hackerrank.com/challenges/nested-list/problem
# Nested Lists
# records = []
# for _ in range(int(input('Enter number of records: '))):
#     name = input('Enter name: ')
#     score = float(input('Enter score: '))
#     records.append([name, score])

# # Extracting the scores using list comprehension
# scores = [score for name, score in records]
# print(scores)
# # Finding the second lowest score
# second_lowest_score = sorted(set(scores))[1]
# print('Second lowest score is: ' + str(second_lowest_score))

# # Finding all names with the second lowest score
# result_names = [name for name, score in records if score == second_lowest_score]
# for name in sorted(result_names):
#     print(name)

# https://www.hackerrank.com/challenges/python-print/problem
# Print Function
n = int(input('Enter a number: '))
result = ''
for i in range(1, n + 1):
    result += str(i)
print(result)