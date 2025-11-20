def SS(List):
    Lenght=len(List)
    for i in range(Lenght):
        Small=i
        for j in range (i+1,Lenght):
            if List[j]<List[Small]:
                Small=j
        List[i],List[Small]=List[Small],List[i]
    return List
List=[int(i) for i in input("Give the List=").split()]
result=SS(List)
print(result)