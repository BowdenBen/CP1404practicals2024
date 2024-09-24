"""
Inputs should be:

daily use in kWh, and
number of days in the billing period.

Example use:

Electricity bill estimator
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75
"""
""" Constants used"""
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff_select = input("Enter tariff, 11 or 31: ") # Get user input selection
while tariff_select != "11" and tariff_select != "31": #while loop for error checking tariff select
    print("Invalid tariff selected")
    tariff_select = input("Enter tariff, 11 or 31: ")  # Get user input selection

if tariff_select == "11": # if, elif compared
    tariff_rate = TARIFF_11 # if = 11 then put CONSTANT TARIFF_11 into variable tariff_rate
elif tariff_select == "31":
    tariff_rate = TARIFF_31


daily_use = int(input("Enter daily use in kWh: ")) # Get user input
billing_days = int(input("Enter number of billing days: "))
estimated_bill = tariff_rate * daily_use * billing_days # Generate estimated bill from user inputs
print(f"Estimated bill: ${estimated_bill:.2f}") # Print estimated bill
