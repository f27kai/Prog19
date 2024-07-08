"""
    ТЕМА: ООП
"""

# class Car:
#     marka = "BMW"
#     year = 2022
#     model = "BMW Х5"
#
# bmw = Car()
# print(f"MARKA: {bmw.marka}\n"
#       f"YEAR: {bmw.year}\n"
#       f"MODEL: {bmw.model}")
# print()
# lexus = Car()
# lexus.marka = "Lexus"
# lexus.year = 2022
# lexus.model = "LEXUS LS"
# print(f"MARKA: {lexus.marka}\n"
#       f"YEAR: {lexus.year}\n"
#       f"MODEL: {lexus.model}")


class Car:

    def __init__(self, marka, year, model):
        self.marka = marka
        self.year = year
        self.model = model

    def get_info(self):
        print(f"MARKA: {self.marka}\n"
              f"YEAR: {self.year}\n"
              f"MODEL: {self.model}")

bmw = Car("BMW", 2020, "BMW Х5")
bmw.get_info()
print()
lexus = Car("Lexus", 2022, "LEXUS LS")
lexus.get_info()
