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

if dia == "+":
    result = plus(a, b)
    print("Результат: ", result)

elif dia == "-":
      result = minus(a, b)
      print("Результат: ", result)

elif dia == "*":
    result = mul(a, b)
    print("Результат: ", result)

elif dia == "/":
    result = div(a, b)
    print("Результат: ", result)

else:
      print("Невідома дія!")