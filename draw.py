from flask import Flask, render_template, request,jsonify
import datetime as dt
import urllib.request
import snowflake.connector
import json
import base64
from werkzeug.utils import secure_filename
from mainfile.emailsend import*
import os

UPLOAD_FOLDER='static/UPLOAD_FOLDER/'
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def main():
    return render_template("Draw.html")

 
@app.route("/draw",methods=["POST","GET"])
def draw():
    l=[]
    val=""
    l.append(request.form.get("Sharingan"))
    l.append(request.form.get("Captain_America"))
    l.append(request.form.get("7_Deadly_Sins"))
    l.append(request.form.get("Butterfly"))
    l.append(request.form.get("Reinnegan_Sharingan"))
    l.append(request.form.get("Shisui_Uchiha"))
    l.append(request.form.get("Doremon"))
    l.append(request.form.get("Ironman"))
    l.append(request.form.get("Superman"))
    l.append(request.form.get("Batman"))
    l.append(request.form.get("Circle"))
    l.append(request.form.get("Smile"))
    print(l)
    for i in l:
        if i==None:
            continue
        else:
            val=i
            
    str0="python C:\\python_codes\\program\\Coding-is-an-Art-main\\"
    str1=".py"
    exe=str0+val+str1
    print(exe)
    os.system(exe)
    return render_template("Draw.html")
  
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
# inbuilt function which takes error as parameter
def page_not_found(e):
    return render_template("500.html"),500

app.run(debug=True)

     
 
