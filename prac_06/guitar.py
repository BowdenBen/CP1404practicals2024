"""
Time to completion EST: 1 hour
Actual Time to Completion:
"""

class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.namer} ({self.year}) : {self.cost}"

#     Method get_age():
#         Calculate age by subtracting self.year from current year
#         Return age
#
#     Method is_vintage():
#         If get_age() is greater than or equal to 50:
#             Return True
#         Else:
#             Return False
