"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $")) # Sales variable holds a user input
while sales >= 0 : # Loop continues while input is a positive number or 0
    if sales < 1000 : # If sales variable is below 1000
        sales_bonus = sales * 0.1 # Sales_bonus variable is 10% of sales
        print(f"Your Sales Bonus is: $ {sales_bonus:.2f}") # Print sales_bonus
    elif sales >= 1000 : # If sales variable equals or is greater than 1000
        sales_bonus = sales * 0.15 # Sales_bonus variable is %15 of sales
        print(f"Your Sales Bonus is: $ {sales_bonus:.2f}") # Print sales_bonus
    sales = float(input("Enter sales: $"))  # Sales variable holds a user input
print ("Negative number, program is shutting down")
