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

if __name__ == "__main__":
    main()