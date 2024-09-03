def square(a):
    formula = a * a # площадь квадрата
    return formula
a = float(input("Длина стороны квадрата: "))
from math import ceil
rounded = ceil(square(a)) # округление результата вверх

print("Площадь квадрата: " + str (rounded))