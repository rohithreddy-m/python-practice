Strat_Number=int(input("Given the Number="))
End_Number=int(input("Given the Number="))
a=Strat_Number
a2=2
b=0
if End_Number>Strat_Number:
    while a<End_Number+1:
        b=0
        a2=2
        while a2<a:
           if a%a2==0 :
              b+=1
           a2+=1
        if b==0:
           print(a)
        a+=1    
        
else :
    print("You Enterd ronge Number")
    
 
''' for i in range (Strat_Number,End_Number+1):
        a=0
        for i2 in range(2,i):
           if i%i2==0 :
              a+=1
        #if a>0:
           #print(f"{i} is composite Number.")
        if a==0 and i > 1:
           #print(f"{i} is prime Number.")
           print(i,end=" ")
else :
    print("You Enterd ronge Number") '''          