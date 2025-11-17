Number=int(input("Give the last Even you want Number="))
'''Num=1
while Num<=Number:
    if Num%2==0:
        print(f"{Num} is Even Number")
    if Num%2!=0:
        print(f"{Num} is Odd Number")
    Num+=1'''
for Num in range (1,Number+1):
    if Num%2==0:
        print(f"{Num} is Even Number")
    if Num%2!=0:
        print(f"{Num} is Odd Number")