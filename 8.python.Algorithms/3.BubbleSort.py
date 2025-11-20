def BS(List):
    Length=len(List)
    for i in range(Length):
        for j in range (Length-i-1):
            if List[j]>List[j+1]:
                List[j],List[j+1]= List[j+1],List[j]
    return List
Lists=[int(i) for i in input("Give the List=").split()]
Bubble_sort=BS(Lists)
print(Bubble_sort)