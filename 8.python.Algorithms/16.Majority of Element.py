def ME(List):
    highest=List[0]
    for i in List:
        if List.count(i) >List.count(highest) :
            highest=i
    print(highest)
List=[int(i) for i in input("Give the List=").split()]
ME(List)