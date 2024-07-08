"""
    ТЕМА: set, dict
"""

"""Set --- {}"""
# numbers = {True, 1, 1, 2, True, False, 5, 5, 6, 7, 8, 9}
# print(numbers)


# fruits = {"apple", "banana", "cherry"}
# salat = {"apple", "banana", "Mango"}

# print(fruits.union(salat))
# print(fruits.difference(salat))
# print(salat.difference(fruits))
# print(fruits.intersection(salat))
# print(fruits.symmetric_difference(salat))


"""Dict --- {}"""
# person = {
#     "name": "Asan",
#     "surname": "Asanov",
#     "age": 19
# }

# print(person["name"])

# person['name'] = "Bakyt"
# person["hobby"] = "To sing"
# print(person)

person = [
    {
        "name": "Asan",
        "surname": "Asanov",
        "age": 19
    },
    {
        "name": "Аймээрим",
        "surname": "Артыкова",
        "age": 14
    },
    {
        "name": "Умар",
        "surname": "Аманов",
        "age": 11

    },
    {
        "name": "Бакдоолот",
        "surname": "Совхозов",
        "age": 12
    }
]


# name = [
#     {
#         'name': "Batma",
#         'surname': "Asanov",
#         'age': 10
#     },
#     {},
#     {}
# ]

# person.append(name)
print(person)