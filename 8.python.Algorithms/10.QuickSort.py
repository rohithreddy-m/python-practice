def QS(List):
    if len(List)<=1:
        return List
    Pivot=List[-1]
    Left=[i for i in List[:-1] if i<Pivot]
    Right=[i for i in List[:-1] if i>Pivot]
    return QS(Left)+[Pivot]+QS(Right)
List=[int(i)for i in input("Gvie the List=").split()]
print(QS(List))