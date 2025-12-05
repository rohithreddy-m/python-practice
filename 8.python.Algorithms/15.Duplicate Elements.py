def DE(List):
    b=[]
    for i in List:
        if List.count(i) !=1 and i not in   b:
            b.append(i)       
    print(b)
List=[int(i) for i in input("Give the List=").split()]
DE(List)