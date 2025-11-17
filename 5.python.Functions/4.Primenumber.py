def primenumber(a):
    if a<=1:
        print(" not primeNumber")
        return
    if a==2:
        print("prime Number")
        return
    for i in range (2,a):
        if a%i==0:
            print("Not primeNumber")
            return
    print("primenumber")  
a=int(input("Give the Number="))
primenumber(a)