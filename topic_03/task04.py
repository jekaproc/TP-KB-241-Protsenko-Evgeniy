def find_insert_position(list, value):

    for i, v in enumerate(list):
        if value <= v:
            return i
    return len(list)

sorted_list = [1, 3, 6, 10, 15]
print("Початковий список:", sorted_list)

new_value = int(input("Введіть число для вставки: "))

position = find_insert_position(sorted_list, new_value)
print("Новий елемент", new_value, "треба вставити на позицію:", position)

sorted_list.insert(position, new_value)
print("Список після вставки:", sorted_list)