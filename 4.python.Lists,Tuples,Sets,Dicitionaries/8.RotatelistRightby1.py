Lists=[int(i) for i in input("Give the lists=").split()]
print(f"{Lists[-1:]+Lists[:-1]}")