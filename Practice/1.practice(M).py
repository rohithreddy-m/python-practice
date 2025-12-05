def a(List,Signal):
    b=[]
    i=0
    if Signal == 'D' :
        while i<len(List[1]):
            if i==0 or i%2==0: 
                b.append(List[0][i])
            else:
                b.append(List[1][i])
            i=i+1
        print(b)
    elif  Signal == 'U' :
        while i<len(List[1]):
            if i==0 or i%2==0: 
                b.append(List[1][i])
            else:
                b.append(List[0][i])
            i=i+1
        print(b)

List=[[1,2,3,4,5,9,0],
      [5,6,7,8,1,2,99]]
Signal=input("Give the signal(D,U)= ")
a(List,Signal)







    # for i in range(len(List)):
    #         b.append(List[i][j])
    #         c=c+1
    #         for k in range(d,d+1,2):
    #                 d=d+1
    #                 b.append(List[i][k])
    # print(b)
    # while c<len(List[0]):
    #     b.append(List[0][c])
    #     c=c+2
    # while d<len(List[1]):
    #     b.append(List[1][d])
    #     d=d+2
    # print(b)