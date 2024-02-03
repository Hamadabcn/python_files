# Import the calendar module

import calendar

# Ask the user for the year and month

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Display the calendar for that month and year

print(calendar.month(year, month))
