from datetime import datetime, timedelta

current_date = datetime.now()
print("Current Date and Time:", current_date)

one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday's Date and Time:", yesterday)

print('Day:', current_date.day)
print('Month:', current_date.month)
print('Year:', current_date.year)
print('Hour:', current_date.hour)
print('Minute:', current_date.minute)
print('Second:', current_date.second)