from flask import render_template, request, flash
from app import app


@app.route("/", methods=["GET", "POST"])
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]

    if request.method == "GET":
        return render_template("home.html", name=name, city_names=city_names)

    if request.method == "POST":
        city = request.form["inputcity"]
        flash(city)
        return render_template("home.html", name=name, city_names=city_names)
