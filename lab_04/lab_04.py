
result = []

def inserting(viraz):
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    output = []
    stack = []

    items = viraz.split()

    for item in items:

        # [ 0-9 ]
        if item.isdigit():
            output.append(item)

        # [ ( ]
        elif item == '(':
            stack.append(item)

        # [ ) ]
        elif item == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())

            if not stack:
                raise ValueError("Помилка: неузгоджені дужки")

            stack.pop()

        # [ + - * / ]
        elif item in priority:
            while (
                stack
                and stack[-1] in priority
                and priority[stack[-1]] >= priority[item]
            ):
                output.append(stack.pop())

            stack.append(item)

        else:
            raise ValueError(f"Невідомий символ: {item}")

    # Очищення стеку
    while stack:
        if stack[-1] in '()':
            raise ValueError("Помилка: неузгоджені дужки")
        output.append(stack.pop())

    return ' '.join(output)


def calculation(result):
    stack = []
    items = result.split()

    for item in items:

        # [ 0-9 ]
        if item.isdigit():
            stack.append(float(item))

        # [ + - * / ]
        elif item in '+-*/^':
            if len(stack) < 2:
                raise ValueError("Помилка: недостатньо операндів")

            b = stack.pop()
            a = stack.pop()

            match item:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case "/":
                    if b == 0:
                        raise ZeroDivisionError("Помилка: ділення на нуль")
                    stack.append(a / b)
                case "^":
                    stack.append(a ** b)
        else:
            raise ValueError(f"Невідомий символ: {item}")

    if len(stack) != 1:
        raise ValueError("Помилка: некоректний ЗПЗ")

    return stack[0]


while True:
    choice = input("Ввести вираз=(В) | Порахувати вираз=(П) | Вийти=(exit) : ")

    match choice.lower():
        case "в":
            viraz = input("Введіть вираз (через пробіли): ")   # 3 + 4 * 2 / ( 1 - 5 ) ^ 2
            result = inserting(viraz)
            print(f"Зворотний польський запис: \n{result}")

        case "п":    
            if not result:
                print("Помилка: Спочатку введіть ЗПЗ")
                continue
            final_result = calculation(result)
            print(f"Результат обчислень зворотного польського запису: \n{final_result}")

        case "exit":
                print("Приходьте ще!")
                break