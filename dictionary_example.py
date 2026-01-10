
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "CompSci"]
    }
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 21
print(student["courses"])  # Output: ['Math', 'CompSci']

student['name'] = 'Bob'
student['age'] = 22
student['courses'].append('Physics')
print(student)  # Output: {'name': 'Bob', 'age': 22, 'courses': ['Math', 'CompSci', 'Physics']}

# Adding a new key-value pair
student['grade'] = 'A'
print(student)  # Output: {'name': 'Bob', 'age': 22, 'courses': ['Math', 'CompSci', 'Physics'], 'grade': 'A'}