# Import the time and calendar modules
import time
import calendar

# Define a function to display the reminder
def display_reminder():
    # Get the reminder text from the user
    print("What shall I remind you about?")
    text = str(input())

    # Get the reminder date from the user in year, month and day
    print("Enter the reminder date:")
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))

    # Convert the date to seconds since epoch
    date = time.mktime((year, month, day, 0, 0, 0, 0, 0, 0))

    # Get the current time in seconds since epoch
    now = time.time()

    # Calculate the difference between the date and now
    diff = date - now

    # Wait for the specified time
    time.sleep(diff)

    # Print the reminder text
    print(text)

    # Print the calendar for that month and year
    print(calendar.month(year, month))