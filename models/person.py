class Person:

    def __init__(self, name='John Doe', age=30, gender='Not specified', region='Unknown', favorite_food='Not specified'):
        self.name = name
        self.age = age
        self.gender = gender
        self.region = region
        self.favorite_food = favorite_food
        self.animals = []

    def printing(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.region)
        print(self.favorite_food)

    def add_animal(self, animal_to_add):
        self.animals.append(animal_to_add)

    def remove_animal(self, animal_to_remove):
        if animal_to_remove in self.animals:
            self.animals.remove(animal_to_remove)
        else:
            print(f"{animal_to_remove} not found in the zoo.")
