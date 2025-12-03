def DB(Number):
    b=""
    while Number>=1:
        r=Number%2
        b=str(r)+b
        Number=Number//2
    return b
Number=int(input("Give the Number="))
result=DB(Number)    
print(result)          