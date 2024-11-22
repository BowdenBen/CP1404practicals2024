
from unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class."""
    # Create two cars with different reliabilities
    r1 = UnreliableCar(name="Mostly Reliable", fuel=100, reliability=90)
    print(f"Testing {r1.name}")
    for i in range(1, 6):  # Test 5 drives
        distance = r1.drive(20)
        print(f"Attempt {i}: Drove {distance} km. Fuel left: {r1.fuel}")

    r2 = UnreliableCar(name="Mostly Unreliable", fuel=100, reliability=30)
    print(f"\nTesting {r2.name}")
    for i in range(1, 6):  # Test 5 drives
        distance = r2.drive(20)
        print(f"Attempt {i}: Drove {distance} km. Fuel left: {r2.fuel}")


if __name__ == "__main__":
    main()
