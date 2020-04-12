from flask import Flask,request
import json
from flask_cors import CORS,cross_origin
import manager

app = Flask(__name__,static_url_path='',static_folder='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/register",methods=["POST"])
@cross_origin()
def add_registration():
    data = request.data
    object = json.loads(data)
    manager.append_registration(object)
    #advice = manager.send_advice_registration(object)
    return "OK"

# @app.route("/advice")
# @cross_origin()
# def get_advice():
#     advices = []
#     for registration in json.loads(get_registrations()):
#         advice = manager.send_advice_registration(registration)
#         advices.append(advice)
#     return json.dumps(advices)


@app.route("/registrations",methods=["GET"])
def get_registrations():
    registrations = []
    for registration in manager.get_registrations():
        registrations.append(registration)
    return json.dumps(registrations)
    #return json.dumps(manager.get_registrations())

@app.route("/")
def root():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run()