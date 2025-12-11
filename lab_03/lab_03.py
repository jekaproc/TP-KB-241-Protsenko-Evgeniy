# python lab_03.py lab3.csv
from sys import argv
from Utils import Utils
from Student import Student

def main():
    print(f"Script name: {argv[0]}")
    print(f"Input parameter: {argv[1]}")

    filename = argv[1]
    students = Utils.load_csv(filename)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")

        match choice.lower():
            case "c":
                print("New element will be created:")
                name = input("Name: ")
                age = input("Age: ")
                phone = input("Phone: ")
                city = input("City: ")
                students.add(Student(name, age, phone, city))
                students.print_all()
            case "u":
                print("Existing element will be updated")
                name = input("Name to update: ")
                new_name = input("New name: ") or name
                new_age = input("New age: ") or age
                new_phone = input("New phone: ") or phone
                new_city = input("New city: ") or city
                students.update(name, Student(new_name, new_age, new_phone, new_city))
            case "d":
                print("Element will be deleted")
                name = input("Name to delete: ")
                students.delete(name)
            case "p":
                print("List will be printed")
                students.print_all()
            case "x":
                Utils.save_csv(filename, students)
                print("Saved successfully! Shutting down...")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()