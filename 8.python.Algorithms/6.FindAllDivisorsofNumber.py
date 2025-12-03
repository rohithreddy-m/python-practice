def AD(Number):
    result=[]
    for i in range(1,Number+1):
        if Number%i==0:
            result.append(i)
    return result
Number=int(input("Give the Number="))
Result=AD(Number)
print(Result)