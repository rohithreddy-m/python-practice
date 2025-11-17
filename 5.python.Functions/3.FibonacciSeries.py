def fibonacci(a):
    s=[]
    i,j=0,1
    for k in range(1,a+1):
        s.append(i)
        i,j=j,i+j
    return s
a=int(input("Give the Number="))
print(fibonacci(a))
