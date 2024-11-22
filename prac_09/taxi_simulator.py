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
            current_taxi = taxi_selection(current_taxi, taxis)
        elif choice == "d":
            total_bill = drive_selection(current_taxi, total_bill)
        elif choice != "q":
            print("Invalid choice.")

        print(f"Your bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")


def drive_selection(current_taxi, total_bill):
    if current_taxi is None:
        print("You need to choose a valid taxi.")
    else:
        current_taxi.start_fare()
        try:
            distance = int(input("Please choose how far to drive."))
            distance_driven = current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            total_bill += trip_cost
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        except ValueError:
            print("Invalid distance")
    return total_bill


def taxi_selection(current_taxi, taxis):
    print("Taxis Available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    try:
        taxi_choice = int(input("Please choose a Taxi."))
        current_taxi = taxis[taxi_choice]
    except ValueError:
        print("That's not a valid Taxi.")
    return current_taxi


if __name__ == "__main__":
    main()

