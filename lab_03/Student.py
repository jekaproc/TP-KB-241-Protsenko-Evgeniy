class Student:
    def __init__(self, name, age, phone, city):
        self.name = name
        self.age = age
        self.phone = phone
        self.city = city

    def __str__(self):
        return f"Student name is {self.name}, Age is {self.age}, Phone is {self.phone}, City is {self.city}"