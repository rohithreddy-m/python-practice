import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_database")

from flask import Flask,jsonify,request
student=Flask(__name__)

@student.get("/student")
def get_student():
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student_report")
    rows = cursor.fetchall()
    return jsonify(rows)

@student.post("/student")
def post_student():
    Request=request.json
    cursor=conn.cursor()
    cursor.execute("""insert into student_report(Name,Age,Math,Telugu,Hindi,English,Social)
                   values(%(Name)s,%(Age)s,%(Math)s,%(Telugu)s,%(Hindi)s,%(English)s,%(Social)s)""",Request) 
    new_id = cursor.lastrowid
    conn.commit()
    Request["id"]=cursor.lastrowid
    return jsonify(Request)
@student.put("/student")
def put_student():
    Request=request.json
    cursor=conn.cursor()
    cursor.execute("""UPDATE student_report
                   set  Name=%(Name)s,
                        Age=%(Age)s,
                        Math=%(Math)s,
                        Telugu=%(Telugu)s,
                        English=%(English)s,
                        Hindi=%(Hindi)s,
                        Social=%(Social)s
                        WHERE id=%(id)s
                         """,Request)
    conn.commit()
    return jsonify(Request)
    
@student.delete("/student/<int:id>")
def delete_student(id):
    # Request=request.json
    cursor=conn.cursor()
    cursor.execute("Delete From student_report WHERE id=%s ",(id,) )
    conn.commit()
    return "id"
if __name__=="__main__" :  
    student.run(debug=True)