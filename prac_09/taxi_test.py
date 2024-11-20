from taxi import Taxi

def main():
    p1 = Taxi(name='Prius 1', fuel=100, price_per_km=1.23)
    # Drive the car for 40 km
    p1.drive(40)
    print(p1)
    print(f"Fare cost is ${p1.get_fare():.2f}")

    # Restart the meter
    p1.start_fare()

    # Drive the car for 100 km
    distance_driven = p1.drive(100)
    print(f"\nAfter starting a new fare and driving {distance_driven} km:")
    print(p1)
    print(f"Current fare cost is ${p1.get_fare():.2f}")

main()