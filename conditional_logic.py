
# Added comments to explain the code
# The code prompts the user to enter the price of an item.
# It then checks if the price is greater than or equal to $1.00.
# If it is, a tax rate of 7% (0.07) is applied.
# If the price is less than $1.00, no tax is applied (tax rate is 0).
# Finally, it prints out the tax rate.
price = float(input("Enter the price of the item: "))
if price >= 1.00:
    tax = .07
    #print(tax)
else:
    tax = 0
    #print(tax)
print('Tax is: ' + str(tax))

# Demonstrating case sensitivity in string comparison
country = 'CANADA'
if country == 'canada':
    print('Oh look a Canadian')
else:
    print('Not from Canada')
# Using lower() method to make the comparison case-insensitive
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')