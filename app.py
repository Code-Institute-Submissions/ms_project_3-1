import os
import uuid
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# Import Werkzeug security helpers
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Create an instance of Flask
app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# Setup an instance of PyMongo
mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists! Please try again.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration complete!")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check if hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and Password combination")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and Password combination")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        #UI needs to be updated to include all fields
        # add image to database
        recipe_image = None
        result = None
        if 'recipe_image' in request.files:
            recipe_image = request.files['recipe_image']
            if recipe_image.filename != '':
                # generate filename using an uuid
                recipe_image.filename = str(uuid.uuid4())
                result = mongo.save_file(recipe_image.filename, recipe_image)

        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "category_name": request.form.get("category_name"),
            "ingredients": request.form.get("ingredients").split('\n'),
            "method": request.form.get("method").split('\n'),
            "image_filename": recipe_image.filename,
            "image_id": result
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe added!") # not working yet
        
    categories = mongo.db.categories.find()
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find()
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/img_uploads/<filename>")
def img_uploads(filename):
    return mongo.send_file(filename)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
