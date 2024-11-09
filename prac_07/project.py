"""
Time to completion EST: 1 hour
Actual Time to Completion: 2 hours
"""

import datetime

class Project:
    def __init__(self, name, start_date, priority, cost, completion):
        """Initialize a new Project instance with the given attributes."""
        self.name = name
        self.start_date = start_date  # This should be a date object
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return a string representation of the Project object."""
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost: ${self.cost:.2f}, completion: {self.completion}%"

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion == 100

    def update_completion(self, new_completion):
        """Update the completion percentage of the project."""
        self.completion = new_completion

    def update_priority(self, new_priority):
        """Update the priority of the project."""
        self.priority = new_priority

    def __lt__(self, other):
        """Compare projects based on priority for sorting."""
        return self.priority < other.priority



