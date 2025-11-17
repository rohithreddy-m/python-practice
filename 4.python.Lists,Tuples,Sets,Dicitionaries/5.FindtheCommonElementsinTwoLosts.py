lists1=input("Give the list1=").split()
lists2=input("Give the list2=").split()
l=[i for i in lists1 if i in lists2]
print(l)
print([i for i in lists1 if i in lists2])
'''for i in lists1:
    if i in lists2:
        l.append(i)
print(l) '''