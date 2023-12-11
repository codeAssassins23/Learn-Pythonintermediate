### Dates ###

from datetime import datetime

now = datetime.now()


# Formatting general from 1970 for timestamp
timestamp = now.timestamp()
print(timestamp)

year_2023 = datetime(2023 , 1 , 1)

def print_date(date):
    print(date)
    print(date.day)
    print(date.month)
    print(date.minute)
    print(date.second)
    print(date.year)
    print(date.timestamp())

print_date(year_2023)