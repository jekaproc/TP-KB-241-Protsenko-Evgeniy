from functions import plus, minus, mul, div
from datetime import datetime

def log(dia, a, b, result):
    with open("log.txt", "a") as file:
        file.write(f"{a} {dia} {b} = {result}   ({datetime.now().strftime("%H:%M:%S %d-%m-%Y")})\n")

def operations():
    try:
        dia = input("Введіть дію (+,-,*,/): ")

        if dia == "exit":
            print("*Калькулятор вимкнувся*")
            return False
        else:
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))

        match dia:
            case "+":
                result = plus(a, b)

            case "-":
                result = minus(a, b)

            case "*":
                result = mul(a, b)

            case "/":
                result = div(a, b)
            
        print("Результат: ", result)
        log(dia, a, b, result)
        return True
    
    except NameError:
            print("Помилка: Невідома дія!")
    except ValueError:
            print("Помилка: Використовуйте лише числа!")
    except ZeroDivisionError:
            print("Помилка: На нуль ділити не можна!")
            return True