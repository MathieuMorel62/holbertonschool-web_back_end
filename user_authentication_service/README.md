# <p align="center">User Authentication Service</p>

![user](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/5e27c207-1b2f-427c-93b2-dba4af11baba)

## Description
This project implements a complete authentication service using Python, Flask, SQLAlchemy and bcrypt. It includes features such as user modeling, session and token management, integration with Flask, and advanced security features for a robust authentication system.

## Resources
- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
- [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [bcrypt library](https://pypi.org/project/bcrypt/)
- [Guide Flask-User](https://flask-user.readthedocs.io/en/latest/)

## 🛠️ Technologies and Tools Used
- **Python**: Main language for backend development.
- **Flask**: Lightweight web framework for Python applications.
- **SQLAlchemy**: ORM tool for database management.
- **bcrypt**: Used for secure password hashing.

## 📋 Prerequisite
- Python 3.7 or higher
- Flask 1.1.2
- SQLAlchemy 1.3.x
- bcrypt 3.1.7

## 🚀 Installation
1. Clone the repository

```bash
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Run the application

```bash
python app.py
```

## 💡 Use
- To create a new user: `POST /users`
- To connect: `POST /sessions`
- To obtain the user's profile: `GET /profile`

## ✨ Main Features
0. [User model](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/user.py): Create a SQLAlchemy model named 'User' for a database table named `users`.
1. [Create user](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/db.py): Implement the `add_user` method in the `DB` class to add a new user to the database.
2. [Find user](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/db.py): Implement the `find_user_by` method in the `DB` class to find users based on specified attributes.
3. [Update user](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/db.py): Implement the `update_user` method in the `DB` class to update user attributes.
4. [Hash password](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Define a `_hash_password` method to generate a salted hash of a password.
5. [Register user](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement the `register_user` method in the `Auth` class to handle user registration.
6. [Basic Flask app](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/app.py): Set up a basic Flask app with a single GET route.
7. [Register user](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/app.py): Implement an endpoint in the Flask app to register a user.
8. [Credentials validation](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement the `valid_login` method in the `Auth` class to validate user credentials.
9. [Generate UUIDs](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement a `_generate_uuid` function in the `auth` module to create UUID strings.
10. [Get session ID](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement the `create_session` method in the `Auth` class to create a session ID.
11. [Log in](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/app.py): Implement a login function in the Flask app to handle user login.
12. [Find user by session ID](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement `get_user_from_session_id` in the `Auth` class to find a user by session ID.
13. [Destroy session](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement `destroy_session` in the `Auth` class to invalidate a user session.
14. [Log out](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/app.py): Implement a logout function in the Flask app to handle user logout.
15. [User profile](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/app.py): Implement a profile function in the Flask app to handle user profile requests.
16. [Generate reset password token](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement `get_reset_password_token` in the `Auth` class to generate a token for password reset.
17. [Get reset password token](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/app.py): Implement a function in the Flask app to handle password reset token requests.
18. [Update password](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/auth.py): Implement `update_password` in the `Auth` class to update a user's password.
19. [Update password end-point](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/app.py): Implement a function in the Flask app to update user passwords.
20. [End-to-end integration test](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/user_authentication_service/main.py): Perform an end-to-end integration test covering all functionalities.

## 📬 Contact
- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-913b4a62/)
