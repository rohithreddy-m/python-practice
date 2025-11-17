def LS(List,NUmber):
    for i in range(len(List)):
        if List[i]==Number:
            return i
    return ("The Number is Not Found in given list")

List=[int(i) for i in input("Give  the Number=").split()]
Number=int(input("Give the Number="))
result=LS(List,Number)
print(f"The list is = {List} and Number to find ={Number}.The index={result}")