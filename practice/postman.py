from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a POST endpoint
@app.route('/postdata', methods=['POST'])
def post_data():
    # Check if JSON is sent in the request
    if request.is_json:
        # Get the JSON data
        data = request.get_json()

        # Example: Accessing some data from the JSON
        name = data.get('name', 'Guest')
        age = data.get('age', 'Unknown')

        # Return a JSON response
        response = {
            'message': f'Hello {name}, your age is {age}.'
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Request must be in JSON format"}), 400

if __name__ == '__main__':
    app.run(debug=True)
