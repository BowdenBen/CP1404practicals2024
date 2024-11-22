from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi Simulator Program"""
    taxis = [Taxi(name="Prius", fuel=100), SilverServiceTaxi(name="Limo",fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    total_bill = 0.0
    choice = ""

    menu = "q)uit, c)hoose, d)rive"
    print("Let's Drive!")

    while choice != "q":
        print(menu)
        choice = input(">>> ").lower()

        if choice =="c":
            print("Taxis Available:")
            for taxi in taxis:
                print(taxi)
            try:
                taxi_choice = int(input("Please choose a Taxi."))
                current_taxi = taxis[taxi_choice]
            except ValueError:
                print("That's not a valid Taxi.")

"""
While loop set to "doesn't equal q"
    print menu options
    get menu choice
    if statement for menu choice
        q to quit, breaks while loop, displays totals
        c to choose taxi, print taxi list
            try, except (AskForForgiveness) to error check for listed taxi
        d to choose drive
            if, else to ensure taxi has been chosen
            once taxi has been chosen
                try, except (AskForForgiveness) to error check for integer given
        
 
"""