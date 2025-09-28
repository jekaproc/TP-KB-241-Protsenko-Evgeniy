def plus(a, b):
        return a + b

def minus(a, b):
        return a - b

def mul(a, b):
        return a * b

def div(a, b):
        if b != 0:
            return a / b
        return "На нуль ділити не можна!"

while True:
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

        case _:
            print("Невідома дія!")
            continue

    print("Результат: ", result)