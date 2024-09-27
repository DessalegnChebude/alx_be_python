from datetime import datetime, timedelta
def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S") #.strftime("%d/%m/%Y %H:%M:%S")
    # print(current_datetime)
    print(f"Current date and time: {formatted_datetime}")
display_current_datetime()

def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days: "))
    future_date = current_date + timedelta(days = number_of_days)
    # print("Current date:", current_date.strftime("%Y-%m-%d"))
    print("Future date:", future_date.strftime("%Y-%m-%d"))
calculate_future_date()