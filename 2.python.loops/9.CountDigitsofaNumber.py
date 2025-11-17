Number=int(input("Give the Number to Count the Digits="))
Number_abs=abs(Number)
Number_String=str(Number)# it well give zero allso
count_while=0
count_for=0
if Number_abs==0:
    print(f"Give Number is {Number}.The Count of the Number of Digits = 1")
else :
    while Number_abs>0:
        Number_abs//=10
        #print(Number_abs)
        count_for+=1
    print(f"Give Number is {Number}.The Count of the Number of Digits ={count_for}")
    for i in Number_String:
        Number_abs//=10
        count_while+=1
    print(f"Give Number is {Number}.The Count of the Number of Digits ={count_while}")