def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


print("Temperature Converter")
print("---------------------")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

choice = int(input("Enter the source temperature scale (1-3): "))
temp = float(input("Enter the temperature value: "))

if choice == 1:
    print(f"\nCelsius: {temp:.2f} °C")
    print(f"Fahrenheit: {celsius_to_fahrenheit(temp):.2f} °F")
    print(f"Kelvin: {celsius_to_kelvin(temp):.2f} K")

elif choice == 2:
    print(f"\nFahrenheit: {temp:.2f} °F")
    print(f"Celsius: {fahrenheit_to_celsius(temp):.2f} °C")
    print(f"Kelvin: {fahrenheit_to_kelvin(temp):.2f} K")

elif choice == 3:
    if temp < 0:
        print("Kelvin temperature cannot be negative.")
    else:
        print(f"\nKelvin: {temp:.2f} K")
        print(f"Celsius: {kelvin_to_celsius(temp):.2f} °C")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(temp):.2f} °F")

else:
    print("Invalid choice! Please select 1, 2, or 3.")