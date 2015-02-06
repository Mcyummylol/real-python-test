#-------------Flask Hello World --------------#

#import the flask class from the flask module
from flask import Flask

#create the application obj
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

#use decorators to link the function to an url
@app.route("/")

def mainPage():
    return("This is the main page.")

@app.route("/teamevent")

def teamevent():
    return "Team Event contents!"

@app.route("/testMirror/<search_query>")

def search(search_query):
    return search_query

@app.route("/name/<name>")

def indexName(name):
    if name.lower() == "michael":
        return "Hello!!!!, {}".format(name), 200
    else:
        return "Not Found", 404

# start the development serever using the run() method
if __name__ == "__main__":
    app.run()
