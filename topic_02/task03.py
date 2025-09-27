
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

    case "-":
      result = minus(a, b)

    case "*":
        result = mul(a, b)

    case "/":
        result = div(a, b)

    case "_":
        print("Невідома дія")

print("Результат: ", result)