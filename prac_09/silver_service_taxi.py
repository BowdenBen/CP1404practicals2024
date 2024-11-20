
from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """A special Taxi subclass with additional fanciness."""

    flagfall = 4.50  # Class-level constant for SilverServiceTaxi flagfall

    def __init__(self, fanciness, **kwargs):
        """Initialize a SilverServiceTaxi with fanciness and other Taxi attributes."""
        super().__init__(self, **kwargs)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness #fanciness scales the Taxi classes prices per km.

