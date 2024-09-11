from math import ceil
a = float(input("Длина стороны квадрата: "))


def square(a):
    formula = a * a  # площадь квадрата
    return formula


rounded = ceil(square(a))  # округление результата вверх

print("Площадь квадрата: " + str(rounded))
