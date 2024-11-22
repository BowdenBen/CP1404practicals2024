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

    def play(self):
        """Play the band."""
        performances = []
        for musician in self.musicians:
            if musician in musician.instruments: # Check if musician has an instrument
                performances.append(musician.play())
            else:
                performances.append(f"{musician.name} needs ands instrument.")
        return "\n".join(performances)

    def __str__(self):
        """Return a string representation of the band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"