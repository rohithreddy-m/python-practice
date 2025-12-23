from flask import Flask , request , jsonify
import mysql.connector
import pandas
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
    cursor.execute("SELECT * FROM student_data")
    rows=cursor.fetchall()
    cursor.close()
    return jsonify(rows)
@app.post("/student")
def post():
    file=request.files["file"]
    Data=pandas.read_excel(file)
    cursor=conn.cursor()
    for _,row in Data.iterrows():
        cursor.execute(
            "INSERT INTO student_data(Name,Age,Math,Telugu) VALUES (%s,%s,%s,%s)",
        (row["Name"],row["Age"],row["Math"],row["Telugu"]) )
    conn.commit()
    cursor.close() 
    
    return jsonify({
        "message": "Data inserted successfully",
        "rows_inserted": len(Data)
                   })
if __name__=="__main__":
    app.run(debug=True)