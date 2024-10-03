import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", now)

# Get the current date
current_date = datetime.date.today()
print("Current date:", current_date)

# Format the current date and time
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_now)
