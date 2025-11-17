Table=int(input("Give the Number of tables="))
Table_IN=int(input("Give the Number of steps in tables="))
num1=1
num2=1
while num1<=Table:
    num2=1
    print(f"\n{num1} Table")
    print()
    while num2<=Table_IN:
        print(f"{num1} x {num2} ={num1*num2}")
        print()
        num2+=1
    num1+=1
'''for num1 in range (1,Table+1):
    for num2 in range(1,Table_IN+1):
        print(f"{num1} x {num2} ={num1*num2}")'''
