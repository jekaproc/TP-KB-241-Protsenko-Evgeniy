import csv
from Student import Student
from StudentList import StudentList

class Utils:
    def load_csv(filename):
        student_list = StudentList()
        with open(filename, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["Name"], row["Age"], row["Phone"], row["City"])
                student_list.add(student)
        return student_list

    def save_csv(filename, student_list):
        with open(filename, "w", newline="") as file:
            fieldnames = ["Name", "Age", "Phone", "City"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for s in student_list.students:
                writer.writerow({"Name": s.name, "Age": s.age, "Phone": s.phone, "City": s.city})
                