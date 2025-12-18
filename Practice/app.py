from flask import Flask,jsonify

app=Flask(__name__)

List=[{"Name":"Rohit","Age":11}]

@app.route("/get",methods=["GET"])
def get():
    return jsonify (List)

@app.route("/post",methods=["POST"])
def Post():
    Add={"Name":"Reddy","Age":20}
    List.append(Add)
    return jsonify(List)

@app.route("/put",methods=["PUT"])
def put():
    Replace={"Name":"Rohith Reddy","Age":21}
    for i in List:
        if i["Name"]=="Reddy":
            List.remove(i)
            List.append(Replace)
            return jsonify (List)

@app.route("/patch",methods=["PATCH"])
def patch():
    for i in List:
        if i["Age"]<=11:
            i["Age"]=19
            return jsonify(List)
@app.route("/delete",methods=["DELETE"])
def delete():
    for i in List:
        if i["Age"]==21:
            List.remove(i)
            return jsonify(List)
app.run(debug=True)