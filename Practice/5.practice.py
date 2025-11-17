Year=int(input("Give the Year="))
if Year%100==0:
    if Year%400==0:
        print("leep year")
    else:
        print("Not leep year")
elif Year%4==0:
    print("leep year")
else:
    print("Not leep year")