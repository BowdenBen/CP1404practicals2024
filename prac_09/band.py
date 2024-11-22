from musician import Musician


class Band:
    """Represents a musical band with a name and a list of musicians."""

    def __init__(self, name):
        """Initialise a Band name and a list of musicians"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
            self.musicians.append(musician)  # Add the musician to the list
