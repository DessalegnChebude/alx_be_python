task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bounded = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"{task} is a High priority task"
    case "medium":
        reminder = f"{task} is a Medium priority task"
    case "low":
        reminder = f"{task} is a low priority task"
    case _:
        print(f"{task} is invalid Priority level")
    
if time_bounded == "yes":
    reminder += " It requires immediate attention today!"
    # print(f"Reminde: {reminder}, It requires immediate attention today!")
else:
    reminder += " Consider completing it when you have free time."
    # print(f"Reminder:  {reminder} Consider completing it when you have free time.")
print(f"Reminder: {reminder}")