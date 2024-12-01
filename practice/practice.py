from flask import Flask, request

app = Flask(__name__)

# Landing page
@app.route("/")
def hello_world():
    return "<p>Welcome</p>"

# End point to login
@app.route("/login", methods=['POST','GET'])
def login_user():
    # Data sent in postman is fetched using
    # request is a module which sends and recieves http data(json data{there can be any form like web socket})
    x = request.get_json()
    print("zzzzzzzzz", x)
    return "Complete"

#Running on custom port
if __name__ == '__main__':
    print("Running on custom port, localhost:5001")
    app.run(debug=True, port=5001)