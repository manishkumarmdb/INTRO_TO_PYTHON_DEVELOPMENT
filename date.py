from datetime import datetime, timedelta

current_date = datetime.now()
print('Current Date and Time: ', current_date)

one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday's Date and Time:", yesterday)

print('Day:', current_date.day)
print('Month:', current_date.month)
print('Year:', current_date.year)
print('Hour:', current_date.hour)
print('Minute:', current_date.minute)
print('Second:', current_date.second)

# Taking user input for birthday
birthday = input('Enter your birthday (YYYY-MM-DD): ')
# Converting string input to datetime object
birthday_date = datetime.strptime(birthday, '%Y-%m-%d')
print('Your birthday is on:', birthday_date)
# Calculating next birthday date
next_birthday = birthday_date.replace(year=current_date.year)
print('This year, your birthday will be on:', next_birthday)
