from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('register.html')

@app.route('/demo')
def hello_world1():
    return render_template('login_admin.html')


if __name__ == '__main__':
    app.run(debug=True)

