from datetime import datetime, timedelta

current_date = datetime.now()
print("Current Date and Time:", current_date)

one_day = timedelta(days=1)
yesterday = current_date - one_day
print("Yesterday's Date and Time:", yesterday)