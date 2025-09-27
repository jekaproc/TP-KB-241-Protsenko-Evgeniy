
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

elif dia == "-":
      result = minus(a, b)

elif dia == "*":
    result = mul(a, b)

elif dia == "/":
    result = div(a, b)
else:
      print("Невідома дія")

print("Результат: ", result)