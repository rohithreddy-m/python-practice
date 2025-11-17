String=input("Give the Sentenc=")
max_value=0
for i in String:
    count=String.count(i) 
    if  count>max_value :
        max_value=count
        max_cha=i
print(max_cha)