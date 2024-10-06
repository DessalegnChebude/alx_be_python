def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator/denominator
        return f"The result of the division is {result:.2f}"
        
    except ZeroDivisionError:
        return f"Error: Division by zero is not allowed."

    except ValueError:
        print("Error: Invalid input. Please provide numeric values.")
