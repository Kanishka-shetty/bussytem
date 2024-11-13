from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\bus\\bussytem\\practice\\database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}

# Create the database
with app.app_context():
    db.create_all()

# Route to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get data from the request body
    data = request.get_json()

    # Extract username and email from the request data
    username = data.get('username')
    email = data.get('email')

    # Ensure both username and email are provided
    if not username or not email:
        return jsonify({"message": "Username and email are required!"}), 400

    # Create a new User instance
    new_user = User(username=username, email=email)

    try:
        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User created successfully", "user": new_user.to_dict()}), 201
    except Exception as e:
        # In case of an error (e.g., unique constraint violation)
        db.session.rollback()
        return jsonify({"message": "Error creating user", "error": str(e)}), 500

# Route to display a single user by id
@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    # Query the database for the user with the given id
    user = User.query.get(id)

    # If the user doesn't exist, return a 404 error
    if user is None:
        return jsonify({"message": "User not found"}), 404

    # Return the user details as a JSON response
    return jsonify({"user": user.to_dict()}), 200

# Route to display all users
@app.route('/users', methods=['GET'])
def get_all_users():
    # Query the database for all users
    users = User.query.all()

    # Convert each user to a dictionary and return them in a list
    users_list = [user.to_dict() for user in users]

    # Return the list of users as a JSON response
    return jsonify({"users": users_list}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)