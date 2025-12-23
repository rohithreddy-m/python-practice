from flask import Flask , request , jsonify
import mysql.connector
conn=mysql.connector.connect(
     host="localhost",
    user="root",
    password="root",
    database="student_database"    
)
app=Flask(__name__)
@app.get("/student/<name>")
def get(name):
    cursor=conn.cursor(dictionary=True)
    cursor.execute("""select student.id,student.Name ,markes.subject,markes.Markes
                    from student
                    join markes
                    on student.id=Markes.student_id
                    where student.Name=%s
                    """,(name,))
    Data=cursor.fetchall()
    conn.commit()
    cursor.close()
    return jsonify(Data)
if __name__=="__main__":
    app.run(debug=True)