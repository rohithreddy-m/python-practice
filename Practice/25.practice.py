number=input("Give the Number=")
a=0
b=len(number)
number=int(number)
for i in range(1,b+1):
    c=number%10
    a+=c
    number//=10
print(a)