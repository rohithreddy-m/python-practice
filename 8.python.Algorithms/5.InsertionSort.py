def IS(List):
    for i in range(len(List)):
        for j in range(len(List)-1):
            if List[j]>List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    return List
List=[int(i) for i in input("Give the List=").split()]
result=IS(List)
print(result)