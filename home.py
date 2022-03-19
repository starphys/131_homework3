from flask import Flask

myapp_obj = Flask(__name__)
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@myapp_obj.route("/")
def home():
    return_string = f"""<h1>Welcome {name}!</h1>
        <a href="www.google.com">not google</a>
        <ul>"""
    for city in city_names:
        return_string += f"<li>{city}</li>"
    return_string += "</ul>"
    return return_string


#myapp_obj.run()
