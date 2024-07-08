"""
    ТЕМА: if elif else
"""

# x = 5000
#
# if x == 2500:
#     print("Жок мага 2500$ керек эмес")
# elif x == 5000:
#     print("Мен макулмун")
# elif x > 2500 and x < 4500:
#     print("Мен макул эмесмин")
# else:
#     print("Мен такыр каршымын")

x = int(input("x: "))
option = input("+, -, /, *, %    ")
y = int(input("y: "))

if option == "+":
    print(x + y)
elif option == "-":
    print(x - y)
elif option == "/":
    if y == 0:
        print("Infinity")
    else:
        print(x / y)
elif option == "*":
    print(x * y)
else:
    print((x / 100) * y)

