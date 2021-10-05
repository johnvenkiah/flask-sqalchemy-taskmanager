from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    # Query the database by calling this function (by clicking categories) and
    # retrieve all records from this table and sort them by name

    # Quantifier .all() needs to be at end
    # By using .all() method, this becomes a cursor object sim. to array/list

    # Convert to python list with list method
    categories = list(Category.query.order_by(Category.category_name).all())
    # pass categories var into render template for displaying data on web page

    # categories 1 = var to be used in html, cat. 2 = list above
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
