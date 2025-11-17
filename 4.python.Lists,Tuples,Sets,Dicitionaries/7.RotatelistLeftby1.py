lists=[int(i) for i in input("Give the lists=").split()]
print(lists)
lists.append(lists.pop(0))
print(lists)
