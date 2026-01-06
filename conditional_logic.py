
# Added comments to explain the code
# The code prompts the user to enter the price of an item.
# It then checks if the price is greater than or equal to $1.00.
# If it is, a tax rate of 7% (0.07) is applied.
# If the price is less than $1.00, no tax is applied (tax rate is 0).
# Finally, it prints out the tax rate.
price = float(input("Enter the price of the item: "))
if price >= 1.00:
    tax = 0.07
    #print(tax)
else:
    tax = 0
    #print(tax)
print('Tax is: ' + str(tax))

# Demonstrating case sensitivity in string comparison
country_name = 'CANADA'
if country_name == 'canada':
    print('Oh look a Canadian')
else:
    print('Not from Canada')
# Using lower() method to make the comparison case-insensitive
if country_name.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')

country = input('Enter the country you are from: ')
if country.lower() == 'usa':
    print('You are from the United States')
elif country.lower() == 'united states' or country.lower() == 'united states of america':
    print('You are from the United States')
else:
    print('You are not from the United States')

# Example of using multiple conditions with logical operators
age = 25
if age >= 18 and age <= 65:
    print('You are of working age.')
if age < 18 or age > 65:
    print('You are not of working age.')
# Demonstrating the use of 'and' and 'or' logical operators
if age >= 18 and age <= 65:
    print('You are of working age.')
if age < 18 or age > 65:
    print('You are not of working age.')

# Example of using 'not' operator
is_raining = False
if not is_raining:
    print('It is not raining, you can go outside.')
else:
    print('It is raining, better stay inside.')

# print tax rate for the given usa state
state = input('Enter your USA state abbreviation (e.g., CA for California): ')
if state == 'CA':
    tax = 0.35
    print('Your California state tax rate is: ' + str(tax))
elif state == 'TX':
    tax = 0.25
    print('Your Texas state tax rate is: ' + str(tax))
elif state == 'FL':
    tax = 0.30
    print('Your Florida state tax rate is: ' + str(tax))