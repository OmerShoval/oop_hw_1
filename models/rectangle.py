class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self, rectangle_instance):
        area =  self.height * self.width
        print(f"The Area of {rectangle_instance} is {area}")



