import math

def diskriminant(a, b, c):
    return b**2 - 4*a*c

def solve_quadratic(a, b, c):
    D = diskriminant(a, b, c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        x = -b / (2*a)
        return x
    else:
        return "Немає дійсних коренів"

a = int(input("Введіть значення a: ")) # 1
b = int(input("Введіть значення b: ")) # 6
c = int(input("Введіть значення c: ")) # 5

print('Корені рівняння: ' + str(solve_quadratic(a, b, c)))