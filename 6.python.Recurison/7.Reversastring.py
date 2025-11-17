def string(Name,name):
    if Name==name:
        return  "".join(name)
    Name.reverse()
    return string(Name,name)
Name=list(input("Give the string="))
name=Name.copy()
name.reverse()
print(string(Name,name))