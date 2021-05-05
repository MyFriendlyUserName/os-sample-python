from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Arrow ECS OpenShift Demo!"

if __name__ == "__main__":
    application.run()
