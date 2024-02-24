# <p align="center">Session Authentication</p>

## 📝 Description
This project implements a session authentication system for a web application. It consists of creating, managing and expiring session identifiers, as well as authenticating users through session cookies. Key points include adding an endpoint to retrieve the authenticated user object, creating a session, retrieving a user ID based on a session ID, and managing session cookies.


## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask](https://palletsprojects.com/p/flask/)
- [Guide to session authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Using uuid in Python](https://docs.python.org/3/library/uuid.html)
- [Management of cookies in Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
- [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/en/latest/)
- [REST API Authentication Mechanisms - Only the session auth part](https://www.youtube.com/watch?v=501dpx2IjGY)

## 🛠️ Technologies and Tools Used
- **Flask**: Used to build the web application and manage HTTP requests.
- **Python**: Main programming language used for backend development.
- **uuid**: Python module used to generate unique identifiers for sessions.

## 📋 Prerequisite
- Python 3.7 or newer
- Flask
- A Python virtual environment (recommended)

## 🚀 Installation and Configuration
1. Clone the repository from GitHub:

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Navigate to the project directory:

```sh
cd Session_authentication
```

3. Install the dependencies: 

```sh
pip install -r requirements.txt
```

4. Launch the Flask server:

```sh
python3 -m flask run
```

## 💡 Use
- Access the different endpoints defined in the application to test session authentication.
- Use cookies to maintain a session between the client and the server.

## ✨ Main Features
1. **Basic Authentication**: Access to the user's endpoints.
2. **Session Creation**: Generates a unique session ID for users.
3. **Session management in a database**: Improves the persistence of sessions.
4. **Session Expiration**: Adds an expiration date to session IDs.

## 📂 Project Structure
- **app.py**: Main file to run the Flask application.
- **auth.py**: Contains the authentication logic.
- **user.py**: Contains the user management logic.
- **session_auth.py**: Contains the session authentication logic.
- **session_db.py**: Contains the session database logic.
- **requirements.txt**: Contains the list of dependencies for the project.

## 📝 List of Tasks to be carried out

0. [**And me and me and me!**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/Session_authentication/api/v1): Initial preparation and basic configuration.
1. [**Empty session**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/Session_authentication/api/v1): Creation of the `SessionAuth` class for session management.
2. [**Create a session**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/Session_authentication/api/v1/auth): Implementation of the method to create a session.
3. [**User ID for Session ID**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/auth/session_auth.py): Setting up the method to link a user ID to a session ID.
4. [**Before request**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/auth/auth.py): Update the `@app.before_request` method in `api/v1/app.py`.
5. [**New view for Session Authentication**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/app.py): Creation of a new Flask view to manage all session authentication routes.
6. [**Login and Logout Routes**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/auth/session_auth.py): Implementation of routes for connection and disconnection.
7. [**Session Expiration**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/auth/session_auth.py): Added an expiration date to the session IDs.
8. [**Logout**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/auth/session_auth.py): Development of the disconnect functionality.
9. [**Expiration?**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/auth/session_exp_auth.py): Added session expiration management.
10. [**Sessions in database**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Session_authentication/api/v1/auth/session_db_auth.py): Storage of sessions in a database for improved persistence.

## 📬 Contact
- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-913b4a62/)
