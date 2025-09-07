from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from pymongo import MongoClient
from bson import ObjectId
import os
from datetime import datetime, UTC

mongo_uri = os.environ.get("MONGO_URI")
db_name = os.environ.get("DB_NAME")

# client = MongoClient("mongodb://mongo:27017/")
# mydb = client["mydatabase"]
client = MongoClient(mongo_uri)
mydb = client[db_name]
mycol = mydb["routers"]
interface_status = mydb["interface_status"]
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
    if ip and username and password:
        # Insert into routers collection
        # data.append({"ip": ip, "username":
        #  username, "password":password})
        mycol.insert_one({"ip": ip, "username": username,
        "password": password})

        # Insert also into interface_status collection
        interface_status.insert_one({
            "router_ip": ip,
            "timestamp": datetime.now(UTC),
            "interfaces": []
        })
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

@app.route("/router/<ip>", methods=["GET"])

def router_detail(ip):
    docs = mydb.interface_status.find({"router_ip": ip}
    ).sort("timestamp", -1).limit(3)
    return render_template(
        "router_detail.html",
        router_ip=ip,
        interface_data=docs,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
