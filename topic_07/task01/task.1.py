class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    S = Student(name, age)
    print(f"Name is {S.name}")
    print(f"Name is {S.age}")

main()