for i in range(50,151):
    a=0
    for j in range (2,i):
        if i %j == 0:
            a+=1
    if i>2:
        if a==0:
            print(f"{i}")