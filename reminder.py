# Import the time module
import time

# Define a function to display the reminder
def display_reminder():
    # Get the reminder text from the user
    print("What shall I remind you about?")
    text = str(input())

    # Get the reminder time from the user in minutes
    print("In how many minutes?")
    local_time = float(input())

    # Convert minutes to seconds
    local_time = local_time * 60

    # Wait for the specified time
    time.sleep(local_time)

    # Print the reminder text
    print(text)
    