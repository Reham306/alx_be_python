#explore datetime 
from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print("current_date =", current_date)
    dt_string = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted date: ", dt_string)

def  calculate_future_date():
    current_date = datetime.now()
    days = int(input("Enter the number of days: "))
    future_date = current_date + timedelta(days=days)
    print(f"future_date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == '__main__':
    display_current_datetime()
    calculate_future_date()