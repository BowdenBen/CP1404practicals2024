from person import Person


class Student(Person):
    def __init__(self, student_id: int, course: str, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.course = course

    def __repr__(self):
        return f"Student: {self.name}, Age: {self.age()}, ID: {self.student_id}, Course: {self.course}"
