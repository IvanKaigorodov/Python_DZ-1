def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"


year_to_check = int(input("Введите год: "))
is_leap = is_year_leap(year_to_check)  # сохраняем результат в переменную

print(f"год {year_to_check}: {is_leap}")
