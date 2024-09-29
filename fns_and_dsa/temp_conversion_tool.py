FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temprature = float(input("Enter the temperature to convert: "))
        unit_measure = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

        if unit_measure == "c":
            temp_celsius = convert_to_fahrenheit(temprature)
            print(f"{temprature}°C is {temp_celsius}°F")
        elif unit_measure == "f":
            temp_fahrenheit = (convert_to_celsius(temprature))
            print(f"{temprature}°F is {temp_fahrenheit}°C")
        
        else:
            print("Invalid Input choice pls ")
        
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()

