# pytest test_student_list.py
import pytest
from Student import Student
from StudentList import StudentList

def test_add_student():
    group = StudentList()
    s = Student("Dima", 20, "0483", "Odesa")
    group.add(s)

    assert len(group.students) == 1
    assert group.students[0].name == "Dima"

def test_add_sorted():
    group = StudentList()
    group.add(Student("Oleg", 20, "0688", "Lviv"))
    group.add(Student("Anna", 21, "0456", "Kyiv"))

    assert group.students[0].name == "Anna"
    assert group.students[1].name == "Oleg"

def test_delete():
    group = StudentList()
    group.add(Student("Dima", 20, "0483", "Odesa"))
    result = group.delete("Dima")

    assert result is True
    assert len(group.students) == 0

def test_delete_non_existing():
    group = StudentList()
    group.add(Student("Dima", 20, "0483", "Odesa"))
    result = group.delete("Ivan")

    assert result is False
    assert len(group.students) == 1

def test_update():
    group = StudentList()
    group.add(Student("Dima", 20, "0483", "Odesa"))

    new_data = Student("", 22, "", "Kyiv")
    result = group.update("Dima", new_data)

    assert result is True
    assert len(group.students) == 1
    assert group.students[0].age == 22
    assert group.students[0].city == "Kyiv"

def test_update_non_existing():
    group = StudentList()
    group.add(Student("Dima", 20, "0483", "Odesa"))

    result = group.update("Petro", Student("Ivan", 22, "0483", "Kyiv"))

    assert result is False
    assert len(group.students) == 1
    assert group.students[0].name == "Dima"