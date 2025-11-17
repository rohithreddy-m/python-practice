num=int(input())
f=0
for i in range(1,num+1):
    f+=i
print(f)
o=0
p=1

while p<=num:
    o+=p
    p+=1
print(o)