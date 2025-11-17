def Binary(n1,e,n=None,count=0):
    if n==None:
        n=n1[0]
    if e==n:
        return count
    return Binary(n1,e,n1[count+1],count+1)
n1=list(map(int,input("Give the Number=").split()))
e=int(input("Give the Element="))
print(Binary(n1,e))
# print(n1)
# print(e)