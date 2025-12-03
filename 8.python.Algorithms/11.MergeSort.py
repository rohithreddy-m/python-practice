def MS(List):
    if len(List)<=1:
        return List
    
    Mid=len(List)//2
    Left=List[:Mid]
    Right=List[Mid:]
    
    Left=MS(Left)
    Right=MS(Right)
    
    return M(Left,Right)
def M(Left,Right):
    l=[]
    j=0
    i=0

    while j<len(Left) and i <len(Right):
        if Left[j]<Right[i]:
            l.append(Left[j])
            j+=1
        else:
            l.append(Right[i])
            i+=1
        
    l.extend(Left[j:])
    l.extend(Right[i:])

    return l

List=[int(i) for i in input("Give the List=").split()]
result=MS(List)
print(result)
