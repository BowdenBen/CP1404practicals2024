from person import Person
from datetime import datetime

from student import Student
from employee import Employee
from musician import Musician

def main():
    p1 = Person("Jane", datetime(1992, 8, 7))
    print(p1)
    print(p1.age())

    s1 = Student(name="John", date_of_birth=datetime(1998, 4, 28), student_id=123, course="Python")
    print(s1)
    print(s1.age())

    e1 = Employee(name="Sarah", date_of_birth=datetime(1948, 12, 1), salary=20000)
    print(e1)
    print(e1.age())

    m1 = Musician(name="Grundle", date_of_birth=datetime(2005, 6, 30), style='dipshit', play= 400)
    print(m1)
    print(m1.age())


    people = [p1, s1, e1, m1]
    for person in people:
        print(person)


main()