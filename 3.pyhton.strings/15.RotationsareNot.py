String1=input("Give the String=")
String2=input("Give the String=")
DoubleString=String1+String1
if len(String1)!= len(String2):
    print("Not Rotation")
else :
    if String2 in DoubleString:
        print("It is the Rotation")
    else:
        print("Not Rotation")