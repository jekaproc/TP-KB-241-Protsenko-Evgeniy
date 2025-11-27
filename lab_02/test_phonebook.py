# pytest test_phonebook.py
def test_create():
    phonebook = []

    new_item = {"name": "Dima", "age": "20", "phone": "12344321", "city": "Odessa"}
    phonebook.append(new_item)

    assert len(phonebook) == 1
    assert phonebook[0]["name"] == "Dima"
    assert phonebook[0]["city"] == "Odessa"

def test_update():
    phonebook = [{"name": "Anna", "age": "21", "phone": "0658495576", "city": "Chernihiv"}]

    updated = {"name": "Iryna", "age": "32", "phone": "0654364343", "city": "Kyiv"}

    phonebook[0].update(updated)

    assert phonebook[0]["name"] == "Iryna"
    assert phonebook[0]["age"] == "32"
    assert phonebook[0]["phone"] == "0654364343"
    assert phonebook[0]["city"] == "Kyiv"

def test_delete():
    phonebook = [{"name": "Bob", "age": "18", "phone": "0665161482", "city": "Kyiv"},
                 {"name": "Anna", "age": "21", "phone": "0658718576", "city": "Chernihiv"}]

    for i, elem in enumerate(phonebook):
        if elem["name"] == "Bob":
            del phonebook[i]
            break

    assert len(phonebook) == 1
    assert phonebook[0]["name"] == "Anna"