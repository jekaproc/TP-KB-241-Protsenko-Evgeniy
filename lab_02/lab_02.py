# python lab_02.py lab2.csv
from sys import argv
import csv

def loadcsv(filename, phonebook):
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            phonebook.append({"name": row["Name"], "age": row["Age"], "phone": row["Phone"], "city": row["City"]})

def savecsv(filename, phonebook):
    with open(filename, "w", newline="") as file:
        fieldnames = ["Name", "Age", "Phone", "City"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in phonebook:
            writer.writerow({"Name": row["name"], "Age": row["age"], "Phone": row["phone"], "City": row["city"]})

def printAllList(phonebook):
    for elem in phonebook:
        strForPrint = "Student name is " + elem["name"] + ",  Age is " + elem["age"] + ",  Phone is " + elem["phone"] + ",  City is " + elem["city"]
        print(strForPrint)

def addNewElement(phonebook):
    name = input("Please enter student name: ")
    age = input("Please enter student age: ")
    phone = input("Please enter student phone: ")
    city = input("Please enter student city: ")
    newItem = {"name": name, "age": age, "phone": phone, "city": city}
    insertPosition = 0
    for item in phonebook:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    phonebook.insert(insertPosition, newItem)
    print(f"Student {name} has been added")
    return

def deleteElement(phonebook):
    name = input("Please enter name to be deleted: ")
    for item in phonebook:
        if name == item["name"]:
            phonebook.remove(item)
            print(f"Student {name} deleted successfully")
            return
    print("Student wasn`t found")

def updateElement(phonebook):
    name = input("Please enter name to be updated: ")

    for item in phonebook:
        if name == item["name"]:
            phonebook.remove(item)
            new_name = input("Enter new name: ") or item["name"]
            new_age = input("Enter new age: ") or item["age"]
            new_phone = input("Enter new phone: ") or item["phone"]
            new_city = input("Enter new city: ") or item["city"]
            newItem = {"name": new_name, "age": new_age, "phone": new_phone, "city": new_city}

            insertPosition = 0
            for item in phonebook:
                if new_name > item["name"]:
                    insertPosition += 1
                else:
                    break
            phonebook.insert(insertPosition, newItem)
            print("Student name has been updated.")
            print("Student name is " + newItem["name"] + ",  Age is " + newItem["age"] + ",  Phone is " + newItem["phone"] + ",  City is " + newItem["city"])
            return

    print("No such name was found.")

def main():
    print(f"Script name: {argv[0]}")
    print(f"Input parameter: {argv[1]}")

    filename = argv[1]
    phonebook = []
    loadcsv(filename, phonebook)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(phonebook)
                printAllList(phonebook)
            case "U" | "u":
                print("Existing element will be updated")
                updateElement(phonebook)
            case "D" | "d":
                print("Element will be deleted")
                deleteElement(phonebook)
            case "P" | "p":
                print("List will be printed")
                printAllList(phonebook)
            case "X" | "x":
                print("Shutting down...")
                savecsv(filename, phonebook)
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()