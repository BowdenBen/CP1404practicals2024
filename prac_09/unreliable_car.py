import random
from prac_09.car import Car

class UnreliableCar(Car):
    """A Car subclass that only sometimes drives based on its reliability."""
    def __init__(self,reliability, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than its reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        # If the car is unreliable for this drive, it drives 0 km
        return 0