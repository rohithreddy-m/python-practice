Set1=set(int(o) for o in input("Give the set1=").split())
Set2=set(int(o) for o in input("Give the set2=").split())
print(Set1.union(Set2))
print(Set1.intersection(Set2))