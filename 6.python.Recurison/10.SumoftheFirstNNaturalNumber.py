def Sum(n,s=1,a=0):
    if s==n:
        return a
    return Sum(n,s+1,a+s)
n=int(input("Give the Number="))
print(Sum(n+1))