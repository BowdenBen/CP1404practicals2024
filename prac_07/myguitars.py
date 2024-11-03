"""
Time to completion EST: 30 min
Actual Time to Completion:
"""


from guitar import Guitar

def main():
    """Main function to load, display, sort, and re-display guitars."""
    # Load guitars from CSV file
    guitars = load_guitars("guitars.csv") # need to write a function called load_guitars
    print("These are my guitars:")

    # Display unsorted guitars
    display_guitars(guitars) # need to write a function called display_guitars

    # Sort guitars by year and display them
    guitars.sort()  # Uses the __lt__ method in Guitar to sort by year
    print("\nThese are my guitars, sorted by year:")
    display_guitars(guitars)

    # Get new guitars from user and add them to the list
    add_new_guitars(guitars)

    # Save all guitars back to the CSV file
    save_guitars("guitars.csv", guitars)



def load_guitars(filename):
    """
    Load guitars from a CSV file and create Guitar instances.
    Returns:
        list of Guitar: A list of Guitar objects loaded from the file.
    """
    guitars = []
    with open(filename, "r") as file:
        # Skip header row if it exists
        next(file)  # Uncomment this line if there is a header in the CSV file
        for line in file:
            # Split each line by commas
            parts = line.strip().split(',')
            # Parse the parts into name, year, and cost
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            # Create a Guitar object and add it to the list
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """
    Display details of a list of Guitar objects.
    """
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """
    Prompt the user to enter new guitars and add them to the list.
    """
    print("\nAdd new guitars (leave name blank to stop):")
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            # Create and add the new guitar
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{name} ({year}) : ${cost:.2f} added.")
        except ValueError:
            print("Invalid input. Please enter a valid year and cost.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """
    Save all guitars to a CSV file.
    """
    with open(filename, "w") as file:
        # Write header
        file.write("Name,Year,Cost\n")
        for guitar in guitars:
            # Write each guitar's details in CSV format
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    print(f"\nAll guitars have been saved to {filename}")

if __name__ == "__main__":
    main()