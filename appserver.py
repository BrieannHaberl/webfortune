# Don't call this flask.py!
# Documentation for Flask can be found at:
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, abort
import os 

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z'


@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    out = ""
    os.system("fortune > fortune.txt")
    f = open("fortune.txt", "r")
    out = f.read()
    out = "<pre>" + out +"</pre>"
    os.system("re fortune.txt")
    return out
     

@app.route('/cowsay/<message>/')
def cowsay(message):
    out2 =""
    os.system("cowsay " + message + " > cowsay.txt")
    f = open("cowsay.txt", "r")
    out2 = f.read()
    out2 = "<pre>" + out2 + "</pre>"
    os.system("rm cowsay.txt")
    return out2


@app.route('/cowfortune/')
def cowfortune():
    out3 = ""
    os.system("'fortune' | cowsay > cowfortune.txt")
    f = open("cowfortune.txt", "r")
    out3 = f.read()
    out3 = "<pre>"  + out3 + "</pre>"
    os.system("rm cowfortune.txt")
    return out3
