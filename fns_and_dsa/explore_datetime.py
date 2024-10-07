#explore datetime 
from datetime import datetime, timedelta

current_date = datetime.now()

def display_current_datetime():
    print("current_date =", current_date)
    dt_string = current_date.strftime("%d/%m/%Y, %H:%M:%S")

def  calculate_future_date():
    days = int(input("Enter the number of days: "))
    future_date = current_date + timedelta(days=days)
    print(f"future_date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == '__main__':
    display_current_datetime()
    calculate_future_date()