def Markes(Name):
    Deta={"Rohit":{"Name":'Rohith',
                'Age':24,
                "KAM(\'Knowing about Me\')":59,
                "GK(\'General knowledge\')":93,
                'Nature':83,
                'Knowing about the pepple':82},
        "Reddy":{"Name":'Reddy',
                'Age':24,
                "KAM(\'Knowing about Me\')":3,
                "GK(\'General knowledge\')":3,
                'Nature':2,
                'Knowing about the pepple':0}}
    
    for Student in Deta:
        Total=( Deta[Student]["KAM(\'Knowing about Me\')"]+
                Deta[Student]["GK(\'General knowledge\')"]+
                Deta[Student]['Nature']+
                Deta[Student]['Knowing about the pepple'])
        Deta[Student]['Total']=Total
        Deta[Student]['Percentage']=Total/4
        
        if Total/4 >=5:
            Deta[Student]['Result']= ' Congratulations'
        else:
            Deta[Student]['Result']=' Better luck next time'
            
    print(Deta[Name])
# Name=input("Give the Name of the Student=")
# Markes(Name)

def u(List,Name):
    for l in range(len(List)):
        if List[l]["name"]==Name:
            total=0
            for i in List[l]['marks']:
                total=int(i['score'])+total
                List[l]["total"]=total
                if total/len(List[l]['marks']) >=5:
                    List[l][" Percentage"]= total/len(List[l]['marks'])
                    List[l][" Result"]= "Congratulations "
                else:
                    List[l][" Percentage"]= total/len(List[l]['marks'])
                    List[l][" Result"]=' Better luck next time'  
            print(List[l])

List=[{"name": "Rohith","marks": [{"subject": "Math","score": "43"},{"subject": "English","score": "73"},{"subject": "Social","score": "81"}]},
      {"name": "Ramya","marks": [{"subject": "Biology","score": "99"},{"subject": "Science","score": "99"},{"subject":"Zoology","score":"99"}]}]
Name=input("Give the Name=")
u(List,Name)
