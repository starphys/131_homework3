from flask import render_template
from app import app


@app.route("/")
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    return render_template("home.html", name=name, city_names=city_names)
