"""
Time to completion EST: 1 hour
Actual Time to Completion: 30 min
"""

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        current_year = 2024  # Update to current year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
