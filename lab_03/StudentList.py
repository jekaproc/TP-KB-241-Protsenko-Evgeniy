from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def print_all(self):
        for s in self.students:
            print(s)

    def add(self, student: Student):
        insertPosition = 0
        for s in self.students:
            if student.name > s.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, student)
        print(f"Student {student.name} has been added")

    def delete(self, name):
        for i, s in enumerate(self.students):
            if s.name == name:
                del self.students[i]
                print(f"Student {s.name} deleted successfully")
                return True
        print("Student wasn`t found")
        return False
    
    def update(self, name, new_student: Student):
        if self.delete(name):
            self.add(new_student)
            return True
        return False
    