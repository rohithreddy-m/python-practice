def AS(List):
    result=False
    for i in range(len(List)):
        small=i
        for j in range(i+1,len(List)):
            if List[j]<List[small]:
                small=j
                result=True       
        if result:
            break
    print(not result)
            
List=[int(i) for i in input("Give the List=").split()]
AS(List)