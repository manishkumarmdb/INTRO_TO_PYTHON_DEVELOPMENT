###
first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')

sum_result = int(first_number) + int(second_number )
print('The sum of ' + first_number + ' and ' + second_number + ' is: ' + str(sum_result))
print(f'The sum of {first_number} and {second_number} is: {sum_result}')
print('The sum of {} and {} is: {}'.format(first_number, second_number, sum_result))
### Demonstrating other arithmetic operations
difference = int(first_number) - int(second_number)
product = int(first_number) * int(second_number)
quotient = int(first_number) / int(second_number)
print(f'The difference is: {difference}')
print(f'The product is: {product}')
print(f'The quotient is: {quotient}')
