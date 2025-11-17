Number1=int(input("Give the Number1="))
Number2=int(input("Give the Number2="))
Max_number=min(Number1,Number2)
Num=1
if Max_number>0:
   for Num in range (1,Max_number+1):
   #while Num<=Max_number :
      if Number1%Num==0 and  Number2%Num==0 :
         Save=Num
      #Num+=1
   print(Save)
else :
   print(f"Give Number are {Number1} and {Number2} Not Valid")