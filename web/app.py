from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId
import os


mongo_uri  = os.environ.get("MONGO_URI")
db_name    = os.environ.get("DB_NAME")

client = MongoClient("mongodb://mongo:27017/")
mydb = client["mydatabase"]
mycol = mydb["routers"]


app = Flask(__name__)

# data = []

@app.route("/")
def main():
    data = mycol.find()
    return render_template("index.html", data=data)
    

@app.route("/add", methods=["POST"])
def add_router():
    # yourname = request.form.get("yourname")
    # message = request.form.get("message")
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")

    # if yourname and message:
    #     data.append({"yourname": yourname, "message": message})
    # return redirect(url_for("main"))
    if ip and username and password :
        # data.append({"ip": ip, "username": username, "password":password})
        x = mycol.insert_one({"ip": ip, "username": username, "password":password})

    return redirect(url_for("main"))

@app.route("/delete", methods=["POST"])
def delete_comment():
    try:
        idx = ObjectId(request.form.get("idx"))
        # if 0 <= idx < len(data):
        #     data.pop(idx)
        mycol.delete_one({"_id": idx})
        return redirect("/")
        
        
    except Exception:
        pass
    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)