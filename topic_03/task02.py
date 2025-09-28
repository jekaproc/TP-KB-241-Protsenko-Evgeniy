list = [1, 2, 3]
print("Список:", list)

list.extend([4, 6])
print("extend([4, 6]):", list)

list.append(5)
print("append(5):", list)

list.insert(0, 0)
print("insert(0, 0):", list)

list.remove(6)
print("remove(0):", list)

list.sort()
print("sort():", list)

list.reverse()
print("reverse():", list)

list_copy = list.copy()
print("copy():", list_copy)

list.clear()
print("clear():", list)