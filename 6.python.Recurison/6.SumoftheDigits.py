def sum(r,a=0):
    if r==0:
        return a
    b=r%10
    return sum(r//10,a=a+b)
r=int(input("Give the Number="))
print(sum(r))