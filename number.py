### This script performs basic arithmetic operations based on user input.
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

### Demonstrating use of float numbers
first_float = input('Enter the first float number: ')
second_float = input('Enter the second float number: ')
float_sum = float(first_float) + float(second_float)
print(f'The sum of {first_float} and {second_float} is: {float_sum}')

### Demonstrating modulus and exponentiation
modulus = int(first_number) % int(second_number)
exponentiation = int(first_number) ** int(second_number)
print(f'The modulus is: {modulus}')
print(f'The exponentiation is: {exponentiation}')

### Demonstrating floor division
floor_division = int(first_number) // int(second_number)
print(f'The floor division is: {floor_division}')

### Demonstrating type conversion
str_number = '100'
int_number = int(str_number)
float_number = float(str_number)
print(f'String to Integer: {int_number}, String to Float: {float_number}')

### Demonstrating order of operations
result = int(first_number) + int(second_number) * 2 - 5 / 5
print(f'Result of order of operations: {result}')

### Using parentheses to change order of operations
result_with_parentheses = (int(first_number) + int(second_number)) * (2 - 5) / 5
print(f'Result with parentheses: {result_with_parentheses}')

### Demonstrating augmented assignment operators
a = int(first_number)
a += 5
print(f'After augmented addition (a += 5): {a}')
a *= 2
print(f'After augmented multiplication (a *= 2): {a}')
a -= 3
print(f'After augmented subtraction (a -= 3): {a}')
a /= 4
print(f'After augmented division (a /= 4): {a}')
a %= 3
print(f'After augmented modulus (a %= 3): {a}')

### Demonstrating rounding of float numbers
float_num = 5.6789
rounded_num = round(float_num, 2)
print(f'Original float: {float_num}, Rounded to 2 decimal places: {rounded_num}')

### Demonstrating absolute value
negative_num = -20
absolute_value = abs(negative_num)
print(f'Absolute value of {negative_num} is: {absolute_value}')

### Demonstrating power function
base = 3
exponent = 4
power_result = pow(base, exponent)
print(f'{base} raised to the power of {exponent} is: {power_result}')

### Demonstrating maximum and minimum functions
num1 = 15
num2 = 25
maximum = max(num1, num2)
minimum = min(num1, num2)
print(f'Maximum of {num1} and {num2} is: {maximum}')
print(f'Minimum of {num1} and {num2} is: {minimum}')

### Demonstrating conversion between int and float
int_value = 10
float_value = float(int_value)
print(f'Integer value: {int_value}, Converted to float: {float_value}')
float_value2 = 9.99
int_value2 = int(float_value2)
print(f'Float value: {float_value2}, Converted to integer: {int_value2}')

### Demonstrating use of complex numbers
complex_num1 = complex(2, 3)
complex_num2 = complex(4, 5)
complex_sum = complex_num1 + complex_num2
print(f'Sum of complex numbers {complex_num1} and {complex_num2} is: {complex_sum}')

### Demonstrating use of scientific notation
sci_num1 = 1.5e3  # 1.5 * 10^3
sci_num2 = 2.5e-2 # 2.5 * 10^-2
sci_sum = sci_num1 + sci_num2
print(f'Sum of scientific notation numbers {sci_num1} and {sci_num2} is: {sci_sum}')

### Demonstrating use of the divmod function
dividend = 20
divisor = 3
quotient, remainder = divmod(dividend, divisor)
print(f'Divmod of {dividend} and {divisor} gives Quotient: {quotient}, Remainder: {remainder}')

### Demonstrating use of the round function with negative ndigits
num_to_round = 1234.5678
rounded_to_nearest_ten = round(num_to_round, -1)
print(f'Number {num_to_round} rounded to nearest ten is: {rounded_to_nearest_ten}')

### Demonstrating use of the int function with different bases
binary_str = '1010'
octal_str = '12'
hex_str = 'A'
binary_to_int = int(binary_str, 2)
octal_to_int = int(octal_str, 8)
hex_to_int = int(hex_str, 16)
print(f'Binary {binary_str} to Integer: {binary_to_int}')
print(f'Octal {octal_str} to Integer: {octal_to_int}')
print(f'Hexadecimal {hex_str} to Integer: {hex_to_int}')

### Demonstrating use of the float function with scientific notation strings
sci_str1 = '1.23e4'
sci_str2 = '5.67E-3'
float_from_sci1 = float(sci_str1)
float_from_sci2 = float(sci_str2)
print(f'Float from scientific notation string {sci_str1}: {float_from_sci1}')
print(f'Float from scientific notation string {sci_str2}: {float_from_sci2}')

### Demonstrating use of the complex function with real and imaginary parts
real_part = 7
imaginary_part = 8
complex_number = complex(real_part, imaginary_part)
print(f'Complex number with real part {real_part} and imaginary part {imaginary_part} is: {complex_number}')

### Demonstrating use of the abs function with complex numbers
complex_num = complex(-3, 4)
magnitude = abs(complex_num)
print(f'Magnitude of complex number {complex_num} is: {magnitude}')

### Demonstrating use of the pow function with three arguments
base_num = 2
exp_num = 5
mod_num = 3
pow_result = pow(base_num, exp_num, mod_num)
print(f'{base_num} raised to the power of {exp_num} modulo {mod_num} is: {pow_result}')

### Demonstrating use of the round function with no ndigits
num_to_round2 = 7.89
rounded_no_ndigits = round(num_to_round2)
print(f'Number {num_to_round2} rounded with no ndigits is: {rounded_no_ndigits}')

### Demonstrating use of the int function with float strings
float_str1 = '45.67'
int_from_float_str = int(float(float_str1))
print(f'Integer converted from float string {float_str1} is: {int_from_float_str}')

### Demonstrating use of the float function with integer strings
int_str1 = '89'
float_from_int_str = float(int_str1)
print(f'Float converted from integer string {int_str1} is: {float_from_int_str}')

