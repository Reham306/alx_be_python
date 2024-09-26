# daily_reminder.py

def daily_reminder():
    # Prompt the user for task description
    task = input("Enter your task: ").strip()

    # Prompt the user for task priority (high/medium/low)
    priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt if the task is time-sensitive (yes/no)
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Customized reminder message based on priority and time sensitivity
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an undefined priority level"

    # Check if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Output the reminder message
    print(f"\nReminder: {reminder}")

# Run the reminder function
if __name__ == "__main__":
    daily_reminder()
