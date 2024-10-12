"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """
    Main function to display an income report for incomes over a given number of months.
    It collects the income for each month from the user and stores it in a list.
    """
    # Create an empty list to store incomes
    incomes = []

    # Get the number of months from the user
    number_of_months = int(input("How many months? "))

    # Collect the income for each month using a loop
    # Loop starts at 1 and goes up to (and includes) the number of months
    for month in range(1, number_of_months + 1):
        # Prompt the user to enter income for each month
        income = float(input(f"Enter income for month {month}: "))
        # Append the entered income to the 'incomes' list
        incomes.append(income)

    # Call the function to print the income report
    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    """
    Prints a formatted income report showing the income and cumulative total for each month.

    :param incomes: A list of income values entered by the user.
    :param number_of_months: The total number of months for which income was collected.
    """
    # Print the report header
    print("\nIncome Report\n-------------")

    # Initialize the total income accumulator
    total = 0

    # Loop through each month to print income and cumulative total
    for month in range(1, number_of_months + 1):
        # Get the income for the current month from the 'incomes' list
        income = incomes[month - 1]  # Subtract 1 because list indexing starts at 0

        # Add the current month's income to the total cumulative income
        total += income

        # Print the formatted output for the current month, showing income and cumulative total
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


# Call the main function to run the program
main()
