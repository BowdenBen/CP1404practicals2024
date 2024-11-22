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

        elif choice == "d":
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
        elif choice != "q":
            print("Invalid choice.")

        print(f"Your bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")


if __name__ == "__main__":
    main()

