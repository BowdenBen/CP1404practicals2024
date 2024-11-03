"""
Time to completion EST: 1 hour
Actual Time to Completion:
"""

import datetime

class Project:
    """Initialize attributes with parameter values"""
    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = start_date  # Should be a date object
        self.priority = priority
        self.cost = cost
        self.completion = completion


    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost: ${self.cost:.2f}, completion: {self.completion}%"


    def is_complete(self):
        return self.completion == 100


    def update_completion(self, new_completion):
        self.completion = new_completion


    def update_priority(self, new_priority):
        self.priority = new_priority


    def __lt__(self, other):
        return self.priority < other.priority


