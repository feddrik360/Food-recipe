import os
from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import dash
import dash_core_components as dcc
import dash_html_components as html

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config["MONGO_DBNAME"] = 'task_manager'
app.config[
    "MONGO_URI"] = 'mongodb+srv://Feddrik360:Office123@myfirstcluster-qdngs.mongodb.net/myProject?retryWrites=true&w=majority'
# app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/recipe/<object_id>')
def recipe(object_id):
    recipe = mongo.db.Cuisine.find_one({"_id": ObjectId(object_id)})
    return render_template('recipe.html', recipe=recipe)

@app.route('/edit_recipe/<object_id>')
def edit_recipe(object_id):
    recipe = mongo.db.Cuisine.find_one({"_id": ObjectId(object_id)})
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/edited_recipe/<object_id>', methods=['POST'])
def edited_recipe(object_id):
    recipes = mongo.db.Cuisine
    recipes.update({'_id': ObjectId(object_id)},
                   {
                       'Name': request.form.get('Name'),
                       'Time': request.form.get('Time'),
                       'Description': request.form.get('Description'),
                       'Ingredients': request.form.get('Ingredients'),
                       'Instructions': request.form.get('Instructions'),
                       'Image': request.form.get('Image')
                   })
    recipe = mongo.db.Cuisine.find_one({"_id": ObjectId(object_id)})
    return render_template('recipe.html', recipe=recipe)

@app.route('/delete_recipe/<object_id>')
def delete_recipe(object_id):
    mongo.db.Cuisine.remove({'_id': ObjectId(object_id)})
    return render_template('recipes.html')

@app.route('/addrecipe')
def add_recipe():
    return render_template('add_recipe.html')

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.Cuisine
    recipes.insert_one(request.form.to_dict())

    return render_template('recipes.html', recipe=recipes)

@app.route('/recipes')
def recipes():
    recipes = mongo.db.Cuisine.find()
    return render_template("recipes.html", recipes=recipes)

@app.route('/home')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=(os.environ.get('PORT')),
            debug=True)
