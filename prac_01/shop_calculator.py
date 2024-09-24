"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount
 is displayed on the screen.
"""

"""
Get number of items
    check number is greater than 0
    display number of items
    ask for price of each items
        if items total more than $100 apply 10% discount
    display total
"""

number_of_items = int(input("Enter the number of items (0 to quit): "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items (0 to quit): "))

total_price = 0  # Initialize total price

if number_of_items > 0:
    # Inner loop to get the price of each item
    for i in range(1, number_of_items + 1):
        price = float(input(f"Price of item {i}: $"))
        total_price += price

    # Apply a 10% discount if total price is over $100
    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount

# Display the total price formatted to two decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")

print("Thank you and please come again")


