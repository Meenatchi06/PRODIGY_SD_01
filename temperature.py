def convert_temperature():
    # Get temperature value and unit from user
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ")

    # Convert temperature to other units
    if unit.upper() == "C":
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        print(f"{temp} degrees Celsius is equivalent to {fahrenheit} degrees Fahrenheit and {kelvin} Kelvin.")
    elif unit.upper() == "F":
        celsius = (temp - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{temp} degrees Fahrenheit is equivalent to {celsius} degrees Celsius and {kelvin} Kelvin.")
    elif unit.upper() == "K":
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{temp} Kelvin is equivalent to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit.")
    else:
        print("Invalid unit of measurement. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")

convert_temperature()
