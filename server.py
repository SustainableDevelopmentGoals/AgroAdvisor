from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route("/register",methods=["POST"])
def add_registration():
    data = request.data
    object = jsonify(data)

@app.route("/registrations",methods=["GET"])
def get_registrations():
    return "registrations"

if __name__ == "__main__":
    app.run()