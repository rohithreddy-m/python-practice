Number=int(input("Give the Number="))
Number_while=1
while Number_while<=Number:
    Cube=Number_while**3
    print(f"The Cube of {Number_while}={Cube}") 
    Number_while+=1
for i in range (Number,0,-1):
    Cube=i**3
    print(f"The Cube of {i}={Cube}")