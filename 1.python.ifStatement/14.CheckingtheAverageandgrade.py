num1=float(input("Give the English Markes="))
num2=float(input("Give the Mathes Markes="))
num3=float(input("Give the Hindi Markes="))
num4=float(input("Give the Social Markes="))
num5=float(input("Give the Telugu Markes="))
add=num1+num2+num3+num4+num5
Average=add/5
if Average>=90:
    print(f"Averege of the five subjate = {Average} and Grade is A")
elif Average >=75:
    print(f"Averege of the five subjate = {Average} and Grade is B")
elif Average >=50:
    print(f"Averege of the five subjate = {Average} and Grade is C")
else :
    print("YOU GAT ANOTHER CHANCE")