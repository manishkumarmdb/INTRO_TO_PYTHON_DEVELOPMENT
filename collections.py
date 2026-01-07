
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

