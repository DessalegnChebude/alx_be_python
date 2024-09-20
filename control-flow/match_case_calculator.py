num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = 0
operation_type = input("Choose the operation (+, -, *, /):")
match operation_type:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1/num2
            print(f"The result is {result}")
    case _:
        print("invalid operation type pls try again")