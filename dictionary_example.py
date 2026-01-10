
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