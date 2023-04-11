from flask import Flask, request, jsonify

# Step 3: Import the required modules
from werkzeug.security import generate_password_hash, check_password_hash

# Step 4: Set up a dictionary to store user credentials
users = {}

# Step 5: Create the Flask application instance
app = Flask(__name__)

# Step 6: Create the user registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400
    
    if username in users:
        return jsonify({"message": "Username already exists."}), 400

    hashed_password = generate_password_hash(password)
    users[username] = hashed_password

    return jsonify({"message": "User registered successfully."}), 201

# Step 6: Create the user login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    stored_password = users.get(username)

    if stored_password and check_password_hash(stored_password, password):
        return jsonify({"message": "Access granted."}), 200
    else:
        return jsonify({"message": "Access denied."}), 401

if __name__ == '__main__':
    app.run(debug=True)
