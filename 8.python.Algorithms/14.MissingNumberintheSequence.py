def MNS(Lists):
    b=[]
    List=set(Lists)
    n=min(List)
    c=max(List)
    for i in range(n,c+1):
        if  i not in List:
            b.append(i)
    print(b)
Lists=[int(i) for i in input("Give the List=").split()]
MNS(Lists)