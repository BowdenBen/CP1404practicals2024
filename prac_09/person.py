from datetime import datetime


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    def age(self):
        """Calculate and return the age of the person."""
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        # Adjust age if today's date is before the birthday this year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return int(age)


    def __repr__(self):
        return f'Person: {self.name}, Age: {self.age()}'