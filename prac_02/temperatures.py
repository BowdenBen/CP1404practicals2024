"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)



def main():
    choice = input(">>> ").upper() # whether lower or upper case is entered, input is converted to upper case
    while choice != "Q": # While "Q" isn't selected, therefore "Q" ends the while loop
        if choice == "C": # Select to enter a temperature in Celsius
            fahrenheit = celsius_to_fahrenheit()
            print(f"Result: {fahrenheit:.2f} F") # Print the resulting fahrenheit variable
        elif choice == "F": # Select to enter a temperature in Fahrenheit
            celsius = fahrenheit_to_celsius()
            print(f"Result: {celsius:.2f} C") # Print the resulting Celsius variable
        else:
            print("Invalid option") # Any other entry will be rejected as invalid
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")




def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit: "))  # Fahrenheit variable holds that input as a float
    celsius = (fahrenheit - 32) * 5 / 9.0  # Celsius variable is derived from the fahrenheit variable
    return celsius


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))  # Celsius variable holds that input as a float
    fahrenheit = celsius * 9.0 / 5 + 32  # Fahrenheit variable is derived from the celsius variable
    return fahrenheit

main()
