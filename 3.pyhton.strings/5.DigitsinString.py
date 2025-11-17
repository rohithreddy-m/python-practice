Number=input("Give the String=")
Count=0
for i in Number:
    if i.isdigit():
        Count+=1
print(f"Number of Digits {Count}.")