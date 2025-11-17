Num=int(input("Give the value of Number="))
"""for i in range(2,Num+1,2):
    print(f"The Even Number ={i}")"""
i=1
while i<=Num: 
      if not(i%2==0):
        i+=1
        continue
      print(f"The Even Number ={i}")
      i+=1
"""i=2
while i<=Num:
    print(f"The Even Number ={i}")
    i+=2"""