"""a=int(input("Give the Year="))
if a%4:
    if a%100 and a%400:
        print(f"{a} is the Leap Year")
    else :
        print(f"{a} is the Leap Year")
else :
    print(f"{a} is the Not the Leap Year")"""


a=int(input("Give the Year="))
r=a%4
r1=a%100
r2=a%400
if r==0:
    if r1==0:
        if r2==0:
            print(f"{a} is the Leap Year")
        else :
            print(f"{a} is the Not Leap Year")
    else :
        print(f"{a} is the Leap Year")
else :
    print(f"{a} is the Not the Leap Year")