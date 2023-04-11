# Simple User Authentication System using Flask

This is a simple user authentication system using Flask, a lightweight web framework for Python. The system includes two endpoints, /register and /login. The /register endpoint accepts a username and password from a POST request and stores them in a dictionary. The /login endpoint also accepts a username and password from a POST request and checks if they match the stored values. If the username and password are correct, it returns an "Access granted" message, otherwise, it returns an "Access denied" message.

## Installation
Clone this repository.
Install the required packages using pip install -r requirements.txt.
Run the Flask app using python app.py.

### /register
Accepts a POST request with the following form data:

{
    "username": "myusername",
    "password": "mypassword"
}

If the username already exists in the users dictionary, it returns a "Username already taken" message. Otherwise, it adds the username and password to the dictionary and returns a "Registration successful" message.


### /login
Accepts a POST request with the following form data:

{
    "username": "myusername",
    "password": "mypassword"
}

If the username is not found in the users dictionary, it returns a "Username not found" message. If the username is found but the password doesn't match, it returns a "Password incorrect" message. Otherwise, it returns an "Access granted" message.