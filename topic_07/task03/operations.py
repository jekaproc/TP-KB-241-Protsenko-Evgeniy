from functions import plus, minus, mul, div

class Calculator:
      
    def operations(self):
        try:
            dia = input("Введіть дію (+,-,*,/): ")

            if dia == "exit":
                print("*Калькулятор вимкнувся*")
                return False
            else:
                a = float(input("Введіть перше число: "))
                b = float(input("Введіть друге число: "))
   
            result = self.calculation(dia, a, b)
            print("Результат: ", result)
            return True
        
        except NameError:
            print("Помилка: Невідома дія!")
        except ValueError:
            print("Помилка: Використовуйте лише числа!")
        except ZeroDivisionError:
            print("Помилка: На нуль ділити не можна!")
            return True

    def calculation(self, dia, a, b):
        match dia:
            case "+":
                return plus(a, b)
            case "-":
                return minus(a, b)
            case "*":
                return mul(a, b)
            case "/":
                return div(a, b)
            case _:
                raise NameError