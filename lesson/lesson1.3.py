"""
    ТЕМА: цикл while
"""

# i = 10

# while i <= 30:
#     print(i)
#     i += 5

# i = 1
#
# while i < 11:
#     j = 0
#     while j < 11:
#         print(f"{i} * {j} = {i * j}")
#         j += 1
#     i += 1
#     print()

# i = 0
#
# while i < 12:
#     if i == 5:
#         break
#     print(i)
#     i += 1

# i = 0
#
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)


while True:
    option = input("Сенин баллын канча: ")
    if option == "выход":
        print("Finished ...")
        break

    option = int(option)

    if option >= 500:
        x = "Золота"
    elif option >= 360:
        x = "Серебро"
    elif option >= 280:
        x = "Бронза"
    elif option >= 100:
        x = "Простой"
    else:
        x = "Откон жоксун"
    print(f"Сенин сертификатын: {x}")
    print()




