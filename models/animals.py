class Animals:

    def __init__(self, kind, age, name, weight, height):
        self.kind = kind
        self.age = age
        self.name = name
        self.weight = weight
        self.height = height

    def printing(self):
        print(self.name)
        print(self.age)
        print(self.weight)
        print(self.height)
        print(self.kind)

