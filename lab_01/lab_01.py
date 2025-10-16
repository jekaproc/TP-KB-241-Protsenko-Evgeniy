list = [
    {"name":"Bob", "age":"18", "phone":"0665161482", "city":"Kyiv"},
    {"name":"Emma", "age":"21", "phone":"0658718576", "city":"Chernihiv"},
    {"name":"John",  "age":"19", "phone":"0636584154", "city":"Lviv"},
    {"name":"Zack",  "age":"25", "phone":"0684645174", "city":"Chernivtsi"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Age is " + elem["age"] + ",  Phone is " + elem["phone"] + ",  City is " + elem["city"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    age = input("Please enter student age: ")
    phone = input("Please enter student phone: ")
    city = input("Please enter student city: ")
    newItem = {"name": name, "age": age, "phone": phone, "city": city}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")

    for item in list:
        if name == item["name"]:
            list.remove(item)
            new_name = input("Enter new name: ") or item["name"]
            new_age = input("Enter new age: ") or item["age"]
            new_phone = input("Enter new phone: ") or item["phone"]
            new_city = input("Enter new city: ") or item["city"]
            newItem = {"name": new_name, "age": new_age, "phone": new_phone, "city": new_city}

            insertPosition = 0
            for name in list:
                if new_name > name["name"]:
                    insertPosition += 1
                else:
                    break
            list.insert(insertPosition, newItem)
            print("Element has been updated.")
            print("Student name is " + newItem["name"] + ",  Age is " + newItem["age"] + ",  Phone is " + newItem["phone"] + ",  City is " + newItem["city"])
            return

    print("No such name was found.")


def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()