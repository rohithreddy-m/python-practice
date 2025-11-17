Num=int(input("Give the number="))
produact_value=1
for a in range(1,Num+1):
    produact_value*=a
    print(f"{produact_value/a} X {a}={produact_value}")
produact_value=1
a=1
while a<=Num:
    produact_value*=a
    a+=1
    print(produact_value)