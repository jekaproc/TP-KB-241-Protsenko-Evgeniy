def dyskryminant(a, b, c):
    D = b**2 - 4*a*c
    return D
    
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
c = int(input("Введіть значення c: "))
print("Дискримінант = " + str(dyskryminant(a, b, c)))