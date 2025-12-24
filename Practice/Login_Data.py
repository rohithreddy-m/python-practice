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
def Login():
    Data=request.json
    cursor=conn.cursor(dictionary=True)
    cursor.execute("""SELECT * from login WHERE username=%s and password =%s""",(Data["username"],Data["password"]))
    user=cursor.fetchone()
    cursor.close()
    if user:
        return ("login is Done")
    else:
        return("login is Failed") 
if __name__=="__main__":
    app.run()