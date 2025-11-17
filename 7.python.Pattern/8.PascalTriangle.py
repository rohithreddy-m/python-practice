number=int(input("Give the Number="))
j=1
for i in range(number):
    print(" "*(number-i),end="")
    n=1
    for f in range(i+1):
        print(n,end=" ")
        n=n*(i-f)//(f+1)
    print()
# n=int(input("fsdfd="))
# for i in range(n):
#     print(" " * (n - i), end="")
#     num = 1
#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()
