def BS(List,Number):
    List.sort()
    print(List)
    start=0
    end=len(List)-1
    while start<=end:
        Middle=(start+end)//2
        if List[Middle]==Number:
            return Middle
        elif List[Middle] < Number:
            start=Middle+1
        else :
            end=Middle-1
    return -1
    
List=[int(i) for i in input("Give the List=").split()]
Number=int(input("Give the Number="))
result=BS(List,Number)  
if result != -1:
    print(f"The index of given Number is {result}")
else :
    print(f"Given Number is Not there in the given List.")