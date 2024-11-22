from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

"""
Initialise Taxis
    Create list of taxis
    set current (starting taxi to none)
    set starting bill to $0
    
Print welcome message

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