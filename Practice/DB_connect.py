import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_database"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM student_report")
rows = cursor.fetchall()
List=[]
Dictionary={'Name':"",'Age':"",'Math':"",'Telugu':"",'English':"","Hindi":"","Social":""}
for j in rows:
    List=[]
    # print(j)
    count=0
    if count<len(j):
        for key in Dictionary:
            # print(f"{key}'='{j[count]}")
            List.append(f"{key}'='{j[count]}")
            count+=1
    print(List)