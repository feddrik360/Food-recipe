import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

@app.route('/hello')
def hello():
 return 'Hello, World!'

if __name__ == '__main__':
 app.run(debug=True)







print("yo")