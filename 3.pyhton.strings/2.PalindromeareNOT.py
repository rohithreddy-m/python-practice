Name=input("Give the Name=").lower()
Reversed_String=""
for Revers in Name:
    Reversed_String=Revers+Reversed_String
if Name==Reversed_String:
    print(f"Give String is Palindrome.")
else: 
    print(f"Give String is Not Palindrome")