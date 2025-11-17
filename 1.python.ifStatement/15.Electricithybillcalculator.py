prevision_units=int(input("Give the Prevision Unitsd="))
prasent_units=int(input("Give the Prasent Unitsd="))
used_units=prasent_units-prevision_units
fexied_cherges=35
if used_units<=100:
    print(f"This Month Used Units are {used_units}. and Total Bill is {used_units*3+fexied_cherges}")
elif used_units<=300:
    print(f"This Month Used Units are {used_units}. and Total Bill is {((100*3)+(used_units-100)*7)+fexied_cherges}")
else :
    print(f"This Month Used Units are {used_units}. and Total Bill is {((100*3)+(200*7)+((used_units-300)*10))+fexied_cherges}")