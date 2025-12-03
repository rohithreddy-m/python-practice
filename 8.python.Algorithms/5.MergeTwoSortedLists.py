def MSL(List1,List2):
    MainList=[]
    List1.sort()
    List2.sort()
    print(List1,List2)
    j=0
    i=0
    while j<=len(List1)-1 and i<=len(List2)-1:
        if List1[j]>List2[i]:
            MainList.append(List2[i])
            i+=1
        else:
            MainList.append(List1[j]) 
            j+=1
    MainList.extend(List1[j:])
    MainList.extend(List2[i:])
    return MainList
List1=[int(i) for i in input("Give the List1=").split()]
List2=[int(i) for i in input("Give the List2=").split()]
result=MSL(List1,List2)
print(result)