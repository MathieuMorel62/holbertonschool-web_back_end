# <p align="center">i18n</p>

![i18n](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/c117cb13-7aca-4b86-a6dc-89c48ad6453a)

## 📝 Description
The i18n project is a multilingual web application developed as part of a web programming project. The main objective is to create a Flask application capable of managing several languages, with an emphasis on internationalization and localization. The project involves the use of Babel for the management of translations and the personalization of content according to the user's language.

## 📚 Resources
- [Documentation Flask-Babel](https://python-babel.github.io/flask-babel/)
- [Flash Internationalization Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [Pytz](https://sourceforge.net/directory/software-development/)

## 🛠️ Technologies and Tools Used
- **Flask**: A lightweight web framework in Python, chosen for its simplicity and flexibility.
- **Babel**: A tool to internationalize Python applications, used for its compatibility with Flask and ease of use.
-**Pytz**: A Python library for working with time zones, used to display the current time in different time zones.

## 📋 Prerequisites
- Python 3.8 or higher
- Flask 1.1.2
- Babel 2.9.0
- pytz 2021.1

## 🚀 Installation and Configuration

1. Clone the GitHub repository: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Navigate to the project folder: 

```sh
cd i18n
```

3. Install Flask and Babel:

```sh
pip install Flask
pip install Flask-Babel
```

## 💡 Use
- Launch the application: `python app.py`
- Access the application via a web browser to test the different languages.

## ✨ Main Features
- **Language management**: Allows users to select their preferred language.
- **Local time display**: Displays the current time in different time zones.

## 📝 Task List

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**Basic Flask app**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/0-app.py) | Creation of a Flask application with a template displaying "Welcome to Holberton" and "Hello world". |
| 1 | [**Basic Babel setup**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/1-app.py) | Installation of Babel Flask and configuration of languages and time zones. |
| 2 | [**Get locale from request**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/2-app.py) | Creation of a function to determine the local via the languages accepted in the request. |
| 3 | [**Parametrize templates**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/3-app.py) | Use of gettext to set up templates and translations into English and French. |
| 4 | [**Force locale with URL parameter**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/4-app.py) | Implementation of the local modification via the URL parameters. |
| 5 | [**Mock logging in**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/5-app.py) | Simulation of the behavior of a user connection system. |
| 6 | [**Use user locale**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/6-app.py) | Modification of the get_locale function to use the user's preferred locale. |
| 7 | [**Infer appropriate time zone**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/7-app.py) | Creation of a function to determine the time zone from URL parameters or user settings, with UTC by default. |
| 8 | [**Display the current time**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/i18n/app.py) | Display of the current time on the home page according to the inferred time zone. |


## 📬 Contact
- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
