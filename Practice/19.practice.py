num=int(input())
for l in range(num,num+1):
    for d in range(1,11):
        print(l*d,end="")
h=1
while True:
    print(num*h)
    h+=1
    if h >10:
        break
    