from models.person import *
from models.animals import *
from models.rectangle import *
from models.employess import *


if __name__ == "__main__" :
    person_1 = Person("Omer", 25, "Male", "Israel", "Pasta")
    person_2 = Person("Aviv", 20, "Female", "Israel", "Pizza")
    person_3 = Person("Adi", 21, "Female", "Israel", "Hamburger")

    rectangle_1 = Rectangle(4, 5)
    rectangle_2 = Rectangle(10, 5)

    employee_1 = Employees("Oded", 1998, "Tel Aviv")
    employee_2 = Employees("Ohad", 2000, "Tel Aviv")
    employee_3 = Employees("Or", 1990, "Tel Aviv")

    print(type(person_1))
    print(type(person_2))
    print(type(person_3))

    person_name = getattr(person_3, "name")
    print(person_name)

    setattr(person_1, "name", "Limor")
    print(person_1.name)

    person_2.name = "Amnon"
    print(person_2.name)

    person_1_animals = ["zoo", "sheppered", "tiger"]
    person_1.add_animal(person_1_animals)
    print(person_1.animals)

    person_1.remove_animal("zoo")
    print(person_1.animals)

    rectangle_1.area(rectangle_1)
    rectangle_2.area(rectangle_2)

    employee_1.print_info(employee_1)
    employee_2.print_info(employee_2)
    employee_3.print_info(employee_3)
