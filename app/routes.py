from flask import render_template, request, flash
from app import myobj

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myobj.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html", name=name, city_names=city_names)

    if request.method == "POST":
        user_input = request.form["user_input"]
        flash(user_input)
        return render_template("home.html", name=name, city_names=city_names)
