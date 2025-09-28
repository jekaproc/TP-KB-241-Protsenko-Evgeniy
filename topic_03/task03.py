S = {'a': 1, 'b': 5, 'c': 3}
print("Словник:", S)

S.update({'b': 2, 'd': 4})
print("update({'b': 2, 'd': 4}):", S)

del S['a']
print("del S['a']:", S)

print("keys():", S.keys())

print("values():", S.values())

print("items():", S.items())

S.clear()
print("clear():", S)