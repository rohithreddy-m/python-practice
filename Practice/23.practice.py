number=input("Give the number=")
a=len(number)
number=int(number)
c=0
#for i in range (1,a+1):
i=1
while i<=a:
    b=number%10
    c=c*10+b
    number=number//10
    i+=1
print(c)