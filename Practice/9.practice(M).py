def p(String):
    a=""
    for i in String:
        a=i+a
    print(a)
    # if a==String:
    #     print(f"yes") 
    # else:
    #     print("No")
# String=input("Give the String=")
# p(String) 
def SS(string,ss):
    Result=False
    a=len(ss)
    for i in range(len(string) - a+1):
        if string[i]==ss[0]:
            if string[i:i+a]==ss :
                Result=True
    if Result:        
        print(Result)
    else:
        print(Result)    
# string=input("Give the String=")
# ss=input("Give the sub String=")
# SS(string,ss)
def cs(string):
    count=0
    for i in string:
        count+=1
    print(count)
# string=input("Give the string=")
# cs(string)
def RW(string):
    string=' '+string+' '
    a=" "
    b=0
    for i in range(len(string)):
        if string[i] ==" " :
            a=a+string[i:b:-1]
            b=i
    print(a)
# string=input("Give the string=")
# RW(string)
def TS(string):
    for i in range(len(string)):
        print(string[:i+1])
# string=input("Give the string=")
# TS(string)
def RT(string):
    for i in range(len(string)-1,-1,-1):
        print(i*' '+string[i:])
# string=input("Give the string=")
# RT(string)
def a(List,number):
    for i in List:
        a=number-i
        if a in List:
            print(i,a)
            break
# List=[int(i) for i in input("Give the List=").split()]
# number=int(input("Gvie the Number="))
# a(List,number)
def pn(number):
    c=True
    a="2"
    for i in range(3,number+1, 2):
        c=True
        for j in range(2,i//2+1):
            # print(i, j)
            if i%j==0:
                c=False  
        if c:         
            a=a+" "+str(i)
    print(a)
number=int(input("Give the Number="))
pn(number)