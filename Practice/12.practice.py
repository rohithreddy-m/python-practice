Age=int(input("Give the Age="))
Number=int(input("Give the Number of Tickets="))
if Age <=18:
    print(f"{50*Number}")
elif Age <=50:
    print(f"{100*Number}")
elif Age >50:
    print(f"{70*Number}")
   