Number=int(input("Give the Number="))
len_Number=len(str(Number))
for_Reverse=0
while_Reverse=0
for_Number=Number
while_Number=Number


while while_Number>0:
    Digite=while_Number%10
    while_Reverse=while_Reverse*10+Digite
    while_Number=while_Number//10
print(f"This is while loop ={while_Reverse}")


for i in range (len_Number) :
    Digite=for_Number%10
    for_Reverse=for_Reverse*10+Digite
    for_Number=for_Number//10
print(f"This is for loop ={for_Reverse}")
   
   