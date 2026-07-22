from flask import Flask , request , jsonify
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_database"    
)
app=Flask(__name__)
@app.get("/student")
def get():
    cursor=conn.cursor(dictionary=True)
    cursor.execute("""select student.id,student.Name ,markes.subject,markes.Markes
                    from student
                    join markes
                    on student.id=Markes.student_id""")
    Data=cursor.fetchall()
    Result={}
    for row in Data:
        student_id=row["id"]
        if student_id not in Result:
            Result[student_id]={
                "id":student_id,
                "Name":row["Name"],
                "Markes":[]}
        Result[student_id]["Markes"].append({
            "subject":row["subject"],
            "Markes":row["Markes"]
        })
    conn.commit()
    cursor.close()
    return jsonify(list(Result.values()))
if __name__=="__main__":
    app.run(debug=True)