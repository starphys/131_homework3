from flask import Flask

myapp_obj = Flask(__name__)


@myapp_obj.route("/")
def home():
    name = "Lisa"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    return f"""<h1>Welcome {name}!</h1>
        <a href="https://www.google.com">not google</a>"""


myapp_obj.run()
