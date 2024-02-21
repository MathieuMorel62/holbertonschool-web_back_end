# <p align="center">Personal Data</p>

## 📝 Description
This project focuses on the secure management of personal data. It focuses on critical aspects such as password encryption and the protection of personally identifiable information (PII). The objective is to develop a reliable system for the manipulation and secure storage of personal data, using state-of-the-art computer security techniques.

## 📚 Resources
- [bcrypt Package](https://intranet.hbtn.io/rltoken/rvDYLUTaAWqtkhSQAJf4zA)
- [Logging in Python](https://docs.python.org/3/library/logging.html)
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [Logging to Files, Setting Levels, and Formatting](https://intranet.hbtn.io/rltoken/sxnkG_PQ8BcYeFGWAIRnjg)
- [What Is PII, non-PII, and Personal Data?](https://intranet.hbtn.io/rltoken/foPGuA-2Dz3K1Y40Zc_Qvg)
- [Regular Expression Operations](https://docs.python.org/3/library/re.html)

## Files Test
[User Data CSV File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/%20user_data.csv)

<details>
<summary>Main Test</summary>
<br>

```python
#!/usr/bin/env python3

import logging

"""
Test the filter_datum function
"""
filter_datum = __import__('filtered_logger').filter_datum
print("\nTEST 1")
fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;\n"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))


"""
Test the RedactingFormatter class
"""
RedactingFormatter = __import__('filtered_logger').RedactingFormatter
print("TEST 2")
message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;"
log_record = logging.LogRecord("my_logger", logging.INFO, None, None, message, None, None)
formatter = RedactingFormatter(fields=("email", "ssn", "password"))
print(formatter.format(log_record))


"""
Test the get_logger function
"""
get_logger = __import__('filtered_logger').get_logger
PII_FIELDS = __import__('filtered_logger').PII_FIELDS
print("\nTEST 3")
print(get_logger.__annotations__.get('return'))
print("PII_FIELDS: {}".format(len(PII_FIELDS)))


"""
Test the hash_password function
"""
hash_password = __import__('encrypt_password').hash_password
print("\nTEST 4")
password = "MyAmazingPassw0rd"
print(hash_password(password))
print(hash_password(password))


"""
Test the is_valid function
"""
hash_password = __import__('encrypt_password').hash_password
is_valid = __import__('encrypt_password').is_valid
print("\nTEST 5")
password = "MyAmazingPassw0rd"
encrypted_password = hash_password(password)
print(encrypted_password)
print(is_valid(encrypted_password, password))
```

</details>

## 🛠️ Technologies and Tools Used
- **Python**: Main programming language.
- **bcrypt**: Used for password encryption.
- **MySQL**: Database management system.
- **Python logging**: Used for logging and filtering logs.

## 📋 Prerequisite
- Python 3.7 or newer.
- Linux environment Ubuntu 18.04
- Bcrypt library for Python.
- MySQL Server.

## 🚀 Installation and Configuration
1. Clone the GitHub repository: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Move to the right directory:

```sh
cd personal_data
```

3. Configure the environment variables for the MySQL database (USERNAME, PASSWORD, HOST, DB_NAME).

## ✨ Main Features
- **Obfuscation of PII fields**: Hides personal information in the logs.
- **Log formatting**: Uses custom trainers to secure logs.
- **Password encryption**: Implementation of a `hash_password` function to encrypt passwords.
- **Password validation**: `is_valid` function to compare encrypted passwords with user entries.
- **Secure connection to the database**: Use of environment variables to store database identifiers.

📝 Task List
0. [Regex-ing](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/filtered_logger.py): Obfuscation of PII fields in logs.
1. [Log formatter](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/filtered_logger.py): Creation of custom log trainers.
2. [Create logger](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/filtered_logger.py): Configuration of a logger for log management.
3. [Connect to secure database](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/filtered_logger.py): Secure connection to a database.
4. [Read and filter data](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/filtered_logger.py): Reading and filtering database data.
5. [Encrypting passwords](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/encrypt_password.py): Secure hashing of passwords.
6. [Check valid password](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/personal_data/encrypt_password.py): Validation of hashed passwords.

## Contact
- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
