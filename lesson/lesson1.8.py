"""
    ТЕМА: import
"""

# import person_info
# from person_info import person as p
#
# p("Абийир", "Каныбеков", 14)
# print()
# person_info.person("Asan", "Asanov", 14)


"""
    Текст менен иштеле турган методдор

    пер.isdigit() - жазылган элементтин баары санбы ошону текшерип берет.
    пер.isalpha() - жазылган элементтин баары тамгабы ошону чыгарат.
    пер.isalnum() - сан тамга аралышпы ошону текшерип берет
    пер.islower() - бардык тамга кичине болсо True деп чыгарат, бир эле тамга чон болсо False деп чыгарат
    пер.isupper() - бардык тамга чон болсо True деп чыгарат, бир эле тамга кичине болсо False деп чыгарып берет
    пер.istitle() -биринчи тамга чонбу же кичинеби текшерет
    пер.lower() - тамгалардын баарын кичине кылып салат
    пер.upper() - тамгалардын баарын чон кылып салат
    пер.startwith(Hi) - баштапкы тамгаларды текшерсе болот
    пер.endswith(12) - акыркы соз кайсыл тамга менен бутконун текшерет
    пер.split() -  текстти листке айландырват
    пер.replace(баштапкы маани, кайсыл созго озгортобуз) - Созду озгортуп берет

    пер - бул переменный
"""

# a = "126"
# print(a.isdigit())

# b = "Asan12"
# print(b.isalpha())
#
# c = "Asan27"
# print(c.isalnum())

# cd = "sana"
# print(cd.islower())

# cd = "AsaN"
# print(cd.isupper())
# print(cd.istitle())
#
# cd = "AsaN"
# print(cd.lower())
# print(cd.title())
# print(cd.upper())

# name = input("Atynyz: ")
# print(name.lower())
# print(name.upper())

# NumText = "Hi 123 Sanjar"
# print(NumText.split())
#
#
# print(f"replaceке чейин: {NumText}")
# print("replaceке колдонгондон кийин: ", NumText.replace("123", "Asan"))

# text = "Hello123"
# print(text.startswith("He"))
# print(text.endswith("423"))


# while True:
#     world = input("Enter your text: ")
#
#     if world == "Exit":
#         print("Finished ... ")
#         break
#
#     world = world.lower()
#     print(world.split())
#     print()