import datetime

def get_current_datetime():
    """Returns the current date and time."""
    return datetime.datetime.now()
def format_datetime(dt, format_string="%Y-%m-%d %H:%M:%S"):
    """Formats a datetime object into a string based on the given format."""
    return dt.strftime(format_string)
def parse_datetime(date_string, format_string="%Y-%m-%d %H:%M:%S"):
    """Parses a string into a datetime object based on the given format."""
    return datetime.datetime.strptime(date_string, format_string)
def add_days_to_datetime(dt, days):
    """Adds a specified number of days to a datetime object."""
    return dt + datetime.timedelta(days=days)
def subtract_days_from_datetime(dt, days):
    """Subtracts a specified number of days from a datetime object."""
    return dt - datetime.timedelta(days=days)
def get_difference_between_datetimes(dt1, dt2):
    """Returns the difference between two datetime objects."""
    return dt2 - dt1
def is_leap_year(year):
    """Checks if a given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
def get_day_of_week(dt):
    """Returns the day of the week for a given datetime object."""
    return dt.strftime("%A")
def get_days_in_month(year, month):
    """Returns the number of days in a given month of a specific year."""
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)
    this_month = datetime.date(year, month, 1)
    return (next_month - this_month).days
def convert_timezone(dt, tz_offset):
    """Converts a datetime object to a different timezone based on the given offset in hours."""
    return dt + datetime.timedelta(hours=tz_offset)
def get_week_number(dt):
    """Returns the week number of the year for a given datetime object."""
    return dt.isocalendar()[1]
def get_quarter(dt):
    """Returns the quarter of the year for a given datetime object."""
    return (dt.month - 1) // 3 + 1
def get_start_of_day(dt):
    """Returns a datetime object representing the start of the day (00:00:00) for a given datetime."""
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)
def get_end_of_day(dt):
    """Returns a datetime object representing the end of the day (23:59:59) for a given datetime."""
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)

n = int(input('Enter a number: '))
for i in range(1, n + 1):
    print(i, end='')
    print()  # For a new line after printing numbers

state = input('Enter your USA state abbreviation (e.g., CA for California): ')
if state == 'CA' or state == 'WA':
    tax = 0.35
elif state == 'TX':
    tax = 0.25
elif state == 'FL' or state == 'LA':
    tax = 0.30
else:
    tax = 0.20
print(f'Your {state} tax rate is: ' + str(tax * 100) + ' %')
# Example usage
if __name__ == "__main__":
    current_dt = get_current_datetime()
    print("Current Date and Time:", format_datetime(current_dt))
    future_dt = add_days_to_datetime(current_dt, 10)
    print("Date after 10 days:", format_datetime(future_dt))
    past_dt = subtract_days_from_datetime(current_dt, 10)
    print("Date 10 days ago:", format_datetime(past_dt))
    print("Is 2024 a leap year?", is_leap_year(2024))
    print("Day of the week:", get_day_of_week(current_dt))
    print("Days in February 2024:", get_days_in_month(2024, 2))
    converted_dt = convert_timezone(current_dt, -5)  # Convert to UTC-5
    print("Converted Date and Time (UTC-5):", format_datetime(converted_dt))
    print("Week number:", get_week_number(current_dt))
    print("Quarter of the year:", get_quarter(current_dt))
    start_of_day = get_start_of_day(current_dt)
    end_of_day = get_end_of_day(current_dt)
    print("Start of the day:", format_datetime(start_of_day))
    print("End of the day:", format_datetime(end_of_day))
    print('Your state tax rate is: ' + str(tax))
    print("Difference between future and past date:", get_difference_between_datetimes(past_dt, future_dt))
