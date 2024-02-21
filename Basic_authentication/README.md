# Basic authentication

# 📝 Description
This project aims to implement a basic authentication system in an API. It includes the creation of authentication classes, error management, the use of Base64 for encoding authentication information, and securing API routes. This project provides an in-depth understanding of the authentication mechanism in web applications.

## 📚 Ressources
- [Flask Http Auth](https://flask-httpauth.readthedocs.io/en/latest/)
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY&themeRefresh=1)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Base64 - concept](https://en.wikipedia.org/wiki/Base64)

## 🛠️ Technologies and Tools Used
- `Python 3.7`: Main programming language.
- `Flask`: Web framework used to build the API.
- `Base64`: Used for encoding authentication information.

## 🗂️ Files
### `models/`
- `base.py`: base of all API models - manages serialization to the file.
- `user.py`: user model.

### `api/v1`
- `app.py`: API entry point.
- `views/index.py`: API base endpoints: `/status` and `/stats`.
- `views/users.py`: all user endpoints.

## 🚀 Installation and Configuration
1. Clone the repository:

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Install the dependencies:

```sh
pip3 install -r requirements.txt
```

3. Launch the Flask server: 

```sh
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## ✨ Main Features
1. **Basic Authentication**: Implementation of a simple but effective authentication mechanism.
2. **Error Management**: Manages authentication errors with appropriate messages.
3. **Road Security**: Secures API routes by verifying authentication information.
4. **User Management**: Offers several routes for the creation, update, deletion and recovery of users.

## 🚦 Roads
- `GET /api/v1/status`: returns the status of the API.
- `GET /api/v1/stats`: returns some API statistics.
- `GET /api/v1/users`: returns the list of users.
- `GET /api/v1/users/:id`: returns a user based on the ID.
- `DELETE /api/v1/users/:id`: deletes a user based on the ID.
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional)).
- `PUT /api/v1/users/:id`: updates a user based on the ID (JSON parameters: `last_name` and `first_name`).

## 📝 List of Tasks
0. [**Simple-basic-API**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/Basic_authentication): Creation of a simple API with a user model.
1. [**Error handler: Unauthorized**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/views/index.py): Error handling for unauthorized requests (401).
2. [**Error handler: Forbidden**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/views/index.py): Error handling for prohibited requests (403).
3. [**Auth class**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/auth.py): Creation of a class to manage API authentication.
4. [**Define which routes don't need authentication**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/auth.py): Definition of routes that do not require authentication.
5. [**Request validation!**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/auth.py): Validation of requests to secure the API.
6. [**Basic auth**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/basic_auth.py): Creation of a class for basic authentication.
7. [**Basic - Base64 part**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/basic_auth.py): Management of Base64 encoding in authentication headers.
8. [**Basic - Base64 decode**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/basic_auth.py): Decodes Base64 values.
9. [**Basic - User credentials**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/basic_auth.py): Extraction of user credentials from the decoded Base64 value.
10. [**Basic - User object**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/basic_auth.py): Recovery of the user object from the credentials.
11. [**Basic - Overload current_user - and BOOM!**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/basic_auth.py): Overload of the current_user method to retrieve the user.
12. [**Basic - Allow password with ":"**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/basic_auth.py): Improved method for extracting user credentials, allowing passwords with:.
13. [**Require auth with stars**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Basic_authentication/api/v1/auth/auth.py): Improved the require_auth method to allow the use of * at the end of the excluded paths.

## Contact
- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
