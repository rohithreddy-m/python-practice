from flask import Flask,jsonify,request

app=Flask(__name__)

List=[{"Name":"Rohit","Age":11}]

@app.get("/get")
def get():
    return jsonify (List)

@app.post("/post")
def Post():
    Data=request.json
    List.append(Data)
    return jsonify(List)

@app.put("/put")
def put():
    Data=request.json
    for i in List:
        if i["Name"]== Data["Name"]:
            i.update(Data)
    return jsonify (List)

@app.patch("/patch")
def patch():
    Data=request.json
    for i in List:
        if i["Age"]<=Data:
            i["Age"]=19
    return jsonify(List)
@app.delete("/delete")
def delete():
    Data=request.json
    for i in List:
        if i["Age"]==Data:
            List.remove(i)
    return jsonify(List)
app.run(debug=True)