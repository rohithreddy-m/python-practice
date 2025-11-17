Markes1=int(input("Give the Markes of Telugu="))
Markes2=int(input("Give the Markes of English="))
Markes3=int(input("Give the Markes of Scinece="))
Markes4=int(input("Give the Markes of Mathes="))
Markes5=int(input("Give the Markes of Hindi="))
Average=((Markes1+Markes2+Markes3+Markes4+Markes5)/5)
if Average > 90:
    print(f"{Average}=A grade.")
elif Average>85 :
    print(f"{Average}=B grade.")
else :
    print (f"{Average}=C grade.")