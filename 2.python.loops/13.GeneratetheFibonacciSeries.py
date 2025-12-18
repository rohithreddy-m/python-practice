Number=int(input("Give the last Number="))
num1=0
num2=1
# print(num1,end=" ")

# p=1
# while p<=Number:
#     print(f"{p}",end=" ")
#     p=num1+num2
#     num1=num2
#     num2=p
# print()
num1=0
num2=1
print(num1,num2,end=" ")
for i in range (1,Number):
    p=num1+num2
    if p>=100:
        exit()
    print(f"{p}",end=" ")
    num1=num2
    num2=p
