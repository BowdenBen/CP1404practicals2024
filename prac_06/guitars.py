"""
Time to completion EST: 30 minutes
Actual Time to Completion: 30 minutes
"""

from guitar import Guitar

def main():
    """
    Main function to collect and display a list of guitars.
    This function allows the user to input guitar details, store them in a list,
    and then display the list of guitars along with information about whether they are vintage.
    """
    guitars = [] # Create an empty list to store guitars

    print("My guitars!")

    # Input loop to get guitar details
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost) # Create a new Guitar object with the provided name, year, and cost
        guitars.append(new_guitar) # add it to the list
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ")

    # Print all stored guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1): # Enumerate through the list of guitars, starting the index at 1
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ =="__main__":
    main()