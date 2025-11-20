def LS(List,number):
    for i in range(len(List)):
        if List[i]==number:
            return i
    return ("The Number is Not Found in given list")

List=[int(i) for i in input("Give  the Number=").split()]
number=int(input("Give the Number="))
result=LS(List,number)
print(f"The list is = {List} and Number to find ={number}.The index={result}")