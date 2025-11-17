A,B,C=map(int,input("Give the angles of Triangle=").split())
sum_of_angles=A+B+C
if sum_of_angles==180:
    print(f"The Sum of the angles of Triangle is {sum_of_angles}. it is the Valid Triangle.")
else :
    print(f"The Sum of the angles of Triangle is {sum_of_angles}. it is Not Valid Triangle.")