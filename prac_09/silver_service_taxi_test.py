from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class for correct fare calculation."""
    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi(fanciness=2, name="Luxury Taxi", fuel=100)

    # Start a new fare and drive 18 km
    taxi.start_fare()
    taxi.drive(18)

    # Check the fare
    expected_fare = 48.78  # Expected fare for an 18 km trip
    actual_fare = taxi.get_fare()

    print(f"Testing fare calculation for {taxi.name}...")
    print(f"Expected Fare: ${expected_fare:.2f}, Actual Fare: ${actual_fare:.2f}")

if __name__ == "__main__":
    main()