class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Ім'я {self.name}, студенту {self.age} років"
    
students = []

def main():
    while True:
        name = input("Введіть ім'я: ")
        age = int(input("Введіть вік: "))
        
        s = Student(name, age)
        students.append(s)
        
        print("\nВідсортований список:")
        for student in sorted(students, key=lambda s: s.age):
            print(student)

        Add = input("Добавити ще студента? (так/ні|yes/no)")
        match Add:
            case "yes" | "так":
                continue
            case "no" | "ні":
                print("Завершення роботи...")
                break               
            case _:
                print(f"Невідома команда \nЗавершення роботи...")
                break

main()