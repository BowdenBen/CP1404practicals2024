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


