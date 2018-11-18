from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello there!  Keep on learning and continue to get better.  11/18/2018 6:47 PM.</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')

