#Emma Vukelj
#SoftDev pd6

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my FIRST route for Work2!"

@app.route("/two")
def two():
    return "Welcome to my SECOND route for Work2"

@app.route("/three")
def three():
    return "Welcome to my THIRD route for Work3"

if __name__ == "__main__":
    app.run()
    
