import csv

StudentMarks = []

with open("StudentMarks.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        StudentMarks.append({"name":row["Name"], "mark":row["Marks"]})

def getName(student):
    return student["name"]

def getMark(student):
    return student["mark"]

for elem in sorted(StudentMarks, key=lambda student: student["name"]):
    print(f"Name = {elem['name']}  mark = {elem['mark']}")