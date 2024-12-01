from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome</p>"

#Running on custom port
if __name__ == '__main__':
    print("Running on custom port, localhost:5001")
    app.run(debug=True, port=5001)
    # print("Running on custom port, localhost:5001")
