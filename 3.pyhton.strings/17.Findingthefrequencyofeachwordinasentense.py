String=input("Give the Sentence=").split()
for i in set(String):
    print(f"{i}={String.count(i)}")