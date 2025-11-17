def Fibonacci(i,j,count,Num):
    if Num==count:
        return 
    print(i,end=" ")
    Fibonacci(j,i+j,count+1,Num)
Num=int(input("Give the Number="))
Fibonacci(0,1,0,Num)
# print()
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("\nEnter number of terms: "))
for i in range(n):
    print(f"{i+1} Fibonacci Number ={fibonacci(i)}")



