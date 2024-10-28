"""
Time to completion EST: 30 hour
Actual Time to Completion:
"""

from guitar import Guitar

def main():
    # Create an empty list to store guitars
    guitars = []

    print("My guitars!")

    # Input loop to get guitar details
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        # Create a new Guitar object and add it to the list
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

        print(f"{name} ({year}) : ${cost:.2f} added.")

        name = input("Name: ")

    # Print all stored guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ =="__main__":
    main()