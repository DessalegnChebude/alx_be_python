task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bounded = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bounded ==  "yes":
            print(f"Reminder : {task} is a high priority task that requires immediate attention today!")
        elif time_bounded == "no":
            print(f"Reminder : {task} is a high priority task but doesn't requires immediate attention.")
        else:
            print("invalid input try again")
    case "medium":
        if time_bounded == "yes":
            print(f"Reminder : {task} is a medium priority task that requires immediate attention today!")
        elif time_bounded == "no":
            print(f"Reminder : {task} is a medium priority task that doesn't requires immediate attention.")
        else:
            print("invalid input try again")
    case "low":
        if time_bounded == "yes":
            print(f"Reminder : {task} is a low priority task that requires immediate attention today!")
        elif time_bounded == "no":
            print(f"Reminder : {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print("invalid input try again")
    case _:
        print("invalid input try again")