def NthSE(Number,List):
    if len(List)>=Number:
        for i in range(len(List)):
            swapped=False
            for j in range(len(List)-1-i):
                if List[j]>List[j+1]:
                    List[j],List[j+1]=List[j+1],List[j]
                    swapped=True
            if not swapped:
                break
        print(List[Number-1])
    else:
        print("Give the Valid Number to Find Nth Smallest Element.")
List=[int(i) for i in input("Give the List=").split()]
Number=int(input("Give the Number="))
NthSE(Number,List)