from flask import Flask

myapp_obj = Flask(__name__)


@myapp_obj.route("/")
def home():
    return """HTML"""


myapp_obj.run()
