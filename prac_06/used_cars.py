"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)  # Create a new Car object named "My Car" with 180 units of fuel
    my_car.drive(30)  # Drive "My Car" for 30 km
    print(f"My Car has fuel: {my_car.fuel}") # Print the remaining fuel in "My Car" after driving
    print(my_car)  #Print the string representation of "My Car" using the __str__ method

    # Create a new Car object called "limo"
    limo = Car("Limo", 100)
    limo.add_fuel(20) # Add 20 more units of fuel to "Limo"
    print(f"Limo has fuel: {limo.fuel}") # Print the current amount of fuel in "Limo" after refueling
    limo.drive(115) # Attempt to drive "Limo" for 115 km
    print(limo) # Print the string representation of "Limo" after driving

main()