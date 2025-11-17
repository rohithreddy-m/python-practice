Number1=int(input("Give the Number for Factorial="))
Number2=int(input("Give the Number for Factorial="))
"""for i in range (Number1,Number2+1):
    Factorial=1
    for j in range (i,0,-1):
        Factorial*=j
    print(f"{i}! = {Factorial}")"""

while Number1<Number2+1:
    Factorial=1
    Num=1
    while Num<=Number1:
        Factorial*=Num
        Num+=1
    print(f"{Number1}! = {Factorial}")
    Number1+=1   