class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Ім'я {self.name}, студенту {self.age} років"

def main():
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    S = Student(name, age)
    print(S)

main()