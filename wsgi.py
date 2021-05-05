from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! OpenShift ist super."

if __name__ == "__main__":
    application.run()
