Num=int(input("Give the Number Factorial ="))
Real_Answer=1
'''for i in range(1,Num+1):
    Real_Answer*=i
print(Real_Answer)''' 
while Num > 1:
    Answer=Num*(Num-1)
    Real_Answer*=Answer
    Num-=2
    print(Real_Answer)