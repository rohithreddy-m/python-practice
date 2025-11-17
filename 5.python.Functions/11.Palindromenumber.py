def Palindrome(num):
    b=0
    Num=num
    for i in range (1,len(str(num))+1):
        a=Num%10
        b=(b*10)+a
        Num//=10
    if b==num:
        return "Palindrome"
#        print("Palindrome")
    else:
        return "Not Palindrome"
#        print("not Palindron")
num=int(input("Give the Number="))
print(Palindrome(num))