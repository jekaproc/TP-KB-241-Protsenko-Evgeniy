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

a = float(input("Введіть перше число: "))
dia = input("Введіть дію (+,-,*,/): ")
b = float(input("Введіть друге число: "))

match dia:
    case "+":
        result = plus(a, b)
        print("Результат: ", result)

    case "-":
      result = minus(a, b)
      print("Результат: ", result)

    case "*":
        result = mul(a, b)
        print("Результат: ", result)

    case "/":
        result = div(a, b)
        print("Результат: ", result)

    case _:
        print("Невідома дія!")