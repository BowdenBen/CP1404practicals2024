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

#
#     Define __str__ method:
#         Return formatted string with project details
#
#     Define is_complete method:
#         Return True if completion is 100, otherwise False
#
#     Define update_completion method with parameter new_completion:
#         Set completion to new_completion
#
#     Define update_priority method with parameter new_priority:
#         Set priority to new_priority
#
#     Define __lt__ method with parameter other:
#         Return True if this project’s priority is less than other’s priority


