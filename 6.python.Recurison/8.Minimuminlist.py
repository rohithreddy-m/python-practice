def minmum(lis,count=0,a=None):
    if a==None :
        a=lis[0]
    if len(lis)==count:
        return a
    if a > lis[count]:
        a=lis[count]
    return minmum(lis,count+1,a)
lis=[int(i) for i in input("Give the Number=").split()]
print(minmum(lis))