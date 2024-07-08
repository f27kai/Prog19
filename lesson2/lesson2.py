"""
    ТЕМА: Мурастоо (ООП)
"""

class Building:

    def __init__(self, type, year, city, pupils, floor):
        self.type = type
        self.year = year
        self.city = city
        self.pupils = pupils
        self.floor = floor

    def get_info(self):
        print(f"Type: {self.type}\n"
              f"Year: {self.year}\n"
              f"City: {self.city}\n"
              f"Pupils: {self.pupils}\n"
              f"Floor: {self.floor}")

class School(Building):

    def __init__(self, type, year, city, pupils, floor, library):
        super().__init__(type, year, city, pupils, floor)
        self.library = library

    def get_info(self):
        super().get_info()
        print(f"Library: {self.library}")

class House(Building):

    def __init__(self, type, year, city, pupils, floor, garage):
        super().__init__(type, year, city, pupils, floor)
        self.garage = garage

    def get_info(self):
        super().get_info()
        print(f"Garage: {self.garage}")

school = School("School", 2018, "Bishkek", 2020, 7, "Yes")
school.get_info()
print()
house = House("House", 1998, "Naryn", 5, 2, "Yes")
house.get_info()