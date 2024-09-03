def fizz_buzz():
    n = int(input("Введите число от 1 до n: "))
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0: # если при делении числа на 3 и на 5 в остатке 0 то FizzBuzz 
            print("FizzBuzz")  
        elif i % 3 == 0: # иначе если при делении числа на 3 в остатке 0 то Fizz
             print("Fizz")
        elif i % 5 == 0: # иначе если при делении числа на 5 в остатке 0 то Buzz
             print("Buzz")   
        else: # иначе
             print(i)
 
fizz_buzz()