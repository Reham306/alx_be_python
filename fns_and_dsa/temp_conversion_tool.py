#Globale conversion factors
FEHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FEHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    global FEHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FEHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FEHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FEHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the tempeature to convert: "))
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted:.2f}°F")
        elif unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted:.2f}°C")
        else:
            print("Invalid input for unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()