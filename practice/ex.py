# from flask import Flask, render_template,  request
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return render_template('login.html')

# @app.route('/new', methods=['POST'])
# def hello():
#     if request.method == 'POST':
#         # Fetch data from the form
#         username = request.form['username']
#         password = request.form['password']
#         password2 = request.form['password2']
#         print("tttttttttttttttttttttt", username)
#         print("pppppppppppp", password)
#         print("pppppppppppp", password2)

#         # Process or display the fetched data as needed
#         # return f"Username: {username}, Password: {password}"
#     return render_template('newuser.html')


# if __name__ == '__main__':
#     app.run(debug=True)










from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('login.html')

@app.route('/new', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            password2 = request.form['password2']

            print("Username:", username)
            print("Password:", password)
            print("Re-entered Password:", password2)

            # Further processing or return statements here
        except KeyError as e:
            print(f"Missing form field: {e}")
            return "Form field missing. Please make sure all fields are filled out.", 400

    return render_template('newuser.html')

if __name__ == '__main__':
    app.run(debug=True)
