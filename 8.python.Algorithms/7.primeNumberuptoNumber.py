def PN(Number):
    result=[]
    for i in range(2,Number+1):
        a=True
        for j in range(2,i):
            if i %j==0:
                a=False
        if a:
            result.append(i)
    return result
Number=int(input("Give the Number="))
Result=PN(Number)
print(Result)