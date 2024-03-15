class Employees:
    def __init__(self, name, year_joined, address):
        self.name = name
        self.year_joined = year_joined
        self.address = address

    def print_info(self, employee):
        print(self.name)
        print(self.year_joined)
        print(self.address)
