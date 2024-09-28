FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
while True:
    try:
        temprature = float(input("Enter the temperature to convert: "))
        unit_measure = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

        if unit_measure == "f":
            def convert_to_celsius(fahrenheit):
                celcius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
                print(f"{fahrenheit}°F is {celcius}°C")

                # °C = (32°F − 32) × 5/9
            convert_to_celsius(temprature)
            # print(temp_in_celcius)
        elif unit_measure == "c":
            def convert_to_fahrenheit(celsius):
                fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
                print(f"{celsius}°C is {fahrenheit}°F")
                # 32°C × 9/5) + 32

            convert_to_fahrenheit(temprature)
        elif unit_measure == "exit":
            print("Goodbye!!!!")
            break
        else: 
            print("Invalid Input pls ")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
    


