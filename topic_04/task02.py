def plus(a, b):
        return a + b

def minus(a, b):
        return a - b

def mul(a, b):
        return a * b

def div(a, b):
            return a / b

while True:
    try:
        dia = input("Введіть дію (+,-,*,/): ")

        if dia == "exit":
            print("*Калькулятор вимкнувся*")
            break
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
    
    except NameError:
        print("Помилка: Невідома дія!")
    except ValueError:
        print("Помилка: Використовуйте лише числа!")
    except ZeroDivisionError:
        print("Помилка: На нуль ділити не можна!")