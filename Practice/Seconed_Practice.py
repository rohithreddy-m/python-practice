from flask import Flask , jsonify , request
import mysql.connector

app=Flask(__name__)
conn= mysql.connector.connect(   
    host="localhost",
    user="root",
    password="root",
    database="student_database"
    )
@app.get("/student")
def get_data():
    cursor=conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM name")
    rows=cursor.fetchall()
    cursor.close()
    return jsonify(rows)
@app.post("/student")
def post_data():
    Data=request.json
    cursor=conn.cursor()
    cursor.execute("""insert into Name (Name,age)
                    values(%(Name)s,%(age)s)""",Data)
    conn.commit()
    cursor.close()
    return jsonify({"Message":"Add is Done",
                   "dara":Data})
@app.put("/student")
def Put_data():
    Data=request.json
    cursor=conn.cursor()
    cursor.execute(""" UPDATE Name
                   SET Name=%(Name)s,
                       age=%(age)s
                   WHERE id=%(id)s
                   """,Data)
    conn.commit()
    cursor.close()
    return jsonify(Data)
@app.delete("/student/<int:id>")
def delete_data(id):
    cursor=conn.cursor()
    cursor.execute("DELETE FROM Name WHERE id=%s",(id,))
    conn.commit()
    cursor.close()
    return jsonify(id)
if __name__=="__main__":
    app.run(debug=True)