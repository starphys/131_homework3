from flask import render_template, request, flash
from app import app

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html", name=name, city_names=city_names)

    if request.method == "POST":
        city = request.form["inputcity"]
        flash(city)
        return render_template("home.html", name=name, city_names=city_names)
