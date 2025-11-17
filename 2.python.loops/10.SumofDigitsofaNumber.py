Number=int(input("Give Number for Addition of Digits="))
Number_Original=Number
Negative=False
if Number<0:
    Negative=True
    Number=-Number
Num_for=Number
#Num_for=str(Number)
added_number=0

while Num_for>0:
#for i in Num_for:
    Number_to_add=int(Num_for)%10
    added_number+=Number_to_add
    Num_for=int(Num_for)//10

if Negative:
    added_number=-added_number

print(f"The Addition of Digits of a {Number_Original} ={added_number}")
