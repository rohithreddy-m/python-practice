lists=[int(i) for i in  input("Give the lists=").split()]
b=[[]]
for i in lists:
    c=[]
    for j in b :
        c.append(j+[i])
    b.extend(c)
print(b)

lists = [int(i) for i in input("Give the list=").split()]
all_sublists = [[]]  # start with empty list

for item in lists:
    # take each existing sublist and add current item to make a new sublist
    new_sublists = []
    for sublist in all_sublists:
        new_sublists.append(sublist + [item])
    all_sublists.extend(new_sublists)

print(all_sublists)



lists = [int(i) for i in input("Give the lists=").split()]
all_sublists = [[]]  # start with empty list
for item in lists:
    new_sublists = []
    for sublist in all_sublists:
        new_sublists.append(sublist + [item])  # add current item to existing sublists
    all_sublists.extend(new_sublists)  # add these new sublists to main list
print(all_sublists)
