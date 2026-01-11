
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

students = []
students.append(student)
students.append({"name": "Charlie", "age": 23, "courses": ["Biology", "Chemistry"]})
print(students)
# Output: [{'name': 'Bob', 'age': 22, 'courses': ['Math', 'CompSci', 'Physics'], 'grade': 'A'}, {'name': 'Charlie', 'age': 23, 'courses': ['Biology', 'Chemistry']}]

# Accessing nested data
for s in students:
    print(f"Student Name: {s['name']}, Age: {s['age']}, Courses: {', '.join(s['courses'])}")
# Output:
# Student Name: Bob, Age: 22, Courses: Math, CompSci, Physics
# Student Name: Charlie, Age: 23, Courses: Biology, Chemistry

# Example of checking if a key exists in the dictionary
if 'grade' in student:
    print(f"{student['name']}'s grade is: {student['grade']}")
# Output: Bob's grade is: A

# Example of using get() method
grade = student.get('grade', 'Not Assigned')
print(f"{student['name']}'s grade is: {grade}")
# Output: Bob's grade is: A
missing_key = student.get('hobby', 'No hobby specified')
print(missing_key)  # Output: No hobby specified

# Example of iterating over dictionary keys and values
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: Bob
# age: 22
# courses: ['Math', 'CompSci', 'Physics']
# grade: A

# Example of removing a key-value pair
removed_course = student['courses'].pop()
print(f"Removed course: {removed_course}")
print(student)
# Output: Removed course: Physics
# {'name': 'Bob', 'age': 22, 'courses: ['Math', 'CompSci'], 'grade': 'A'}

# Example of clearing the dictionary
student.clear()
print(student)  # Output: {}