# <p align="center">NoSQL: MongoDB</p>

![mongodb](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/540c2962-edbe-4838-b76d-2aebe9b8efe5)

## 📝 Description
This NoSQL project is designed to provide a thorough and practical understanding of NoSQL databases. It covers the fundamental concepts of NoSQL, the differences from traditional SQL databases, and examples of implementation using **MongoDB**. This project allows users to master basic operations such as inserting, updating, and deleting data, as well as complex queries and data aggregation.

## 📚 Resources
- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL ?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/mongodb-shell/)

## 🛠️ Technologies and Tools Used
- `MongoDB`: A popular NoSQL database, used for its flexibility and performance.
- `Python`: Scripting language to interact with the MongoDB database and manage data.
- `PyMongo`: A MongoDB tool for the Python language, allowing easy interaction with the database.

## 📋 Prerequisite
- MongoDB version 4.2 or higher
- Python version 3.7 or higher
- PyMongo version 3.10 or higher

## 📊 Data Files

- [dump.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/645541f867bb79ae47b7a80922e9a48604a569b9.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240325%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240325T125449Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=d39a83c55f1f14a790b7b53e7a4d36a0b7ecc1fa0d01319f5e1ad9bceeb053ac)

## 🚀 Installation and Configuration

1. Install MongoDB: Follow [this guide](https://docs.mongodb.com/manual/installation/).

2. Configure your Python environment and install PyMongo with: 

```sh
pip3 install pymongo
```

3. Clone the repository: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

4. Navigate to the project folder: 

```sh
cd NoSQL
```

## 💡 Use
- Use the provided Python scripts to interact with the MongoDB database.
- Script files include example requests, insertions, and updates.

## ✨ Main Features
1. **NoSQL data management**: Learn how to create, read, update and delete data.
2. **Complex queries**: Master complex queries and data aggregation.

## 📝 List of Tasks

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**List all databases**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/0-list_databases) | Script to list all databases in MongoDB. |
| 1 | [**Create a database**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/1-use_or_create_database) | Script to create or use a specific database. |
| 2 | [**Insert document**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/2-insert) | Script to insert a document in the 'school' collection. |
| 3 | [**All documents**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/3-all) | Script to list all documents in the 'school' collection. |
| 4 | [**All matches**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/4-match) | Script to list all documents with a specific name in the 'school' collection. |
| 5 | [**Count**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/5-count) | Script to display the number of documents in the 'school' collection. |
| 6 | [**Update**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/6-update) | Script to add a new attribute to a document in the 'school' collection. |
| 7 | [**Delete by match**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/7-delete) | Script to delete all documents corresponding to a criterion in the 'school' collection. |
| 8 | [**List all documents in Python**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/8-all.py) | Python function to list all documents in a collection. |
| 9 | [**Insert a document in Python**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/9-insert_school.py) | Python function to insert a new document into a collection. |
| 10 | [**Change school topics**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/10-update_topics.py) | Python function to modify the topics of a school document. |
| 11 | [**Where can I learn Python?**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/11-schools_by_topic.py) | Python function to return the list of schools with a specific subject. |
| 12 | [**Log stats**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/12-log_stats.py) | Python script providing statistics on Nginx logs stored in MongoDB. |
| 13 | [**Regex filter**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/100-find) | Script to list all documents whose name begins with 'Holberton' in the 'school' collection. |
| 14 | [**Top students**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/101-students.py) | Python function to return all students sorted by average score. |
| 15 | [**Log stats - new version**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/NoSQL/102-log_stats.py) | Improved log statistics script with the most present IPs. |


## 📬 Contact
- Profil LinkedIn : [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
