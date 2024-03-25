# <p align="center">MySQL Advanced</p>

![mysql](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/7fe07492-a84b-48d3-83df-2347148b7fcc)

## 📝 Description
The **MySQL advanced** project is an in-depth exploration of the advanced features of MySQL. This project highlights concepts such as creating tables with constraints, optimizing queries by adding indexes, and implementing stored procedures, functions, views and triggers in MySQL. The main objective is to provide an in-depth understanding of these advanced aspects and to improve MySQL database management skills.

## 📚 Resources
- [MySQL Cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.mysqltutorial.org/mysql-index/mysql-create-index/)
- [Stored Procedure in MySQL](https://www.mysqltutorial.org/mysql-stored-procedure-tutorial.aspx)
- [Triggers in MySQL](https://www.mysqltutorial.org/mysql-triggers.aspx)
- [Views in MySQL](https://www.mysqltutorial.org/mysql-views-tutorial.aspx)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.co)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)
- [Calculate-Weighted-Average](https://www.wikihow.com/Calculate-Weighted-Average)


## 🛠️ Technologies and Tools Used
- **MySQL 5.7**: Used for the creation and manipulation of databases.
- **Ubuntu 18.04 LTS**: Operating system on which SQL scripts are executed.

## 📋 Prerequisite
- MySQL version 5.7.30 or higher
- An Ubuntu 18.04 LTS environment

## 🚀 Installation and Configuration
1. Install `MySQL 5.7` on `Ubuntu 18.04`.
2. Configure the database settings according to the needs of the project.
3. Download Data files [metal_bands.sql.zip](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20240323%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20240323T115412Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=43fcda7c28e96dbaf924313829f9c758b9ad6e967ceae6f0496514a4264382bb) and [names.sql.zip](https://intranet-projects-files.s3.amazonaws.com/holbertonschool-webstack/632/names.sql.zip)

## 💡 Use
To use this project, launch the SQL scripts provided in a MySQL environment. Make sure you respect the order of the scripts for correct execution.

## ✨ Main Features
1. **Creation of tables with constraints**: Learn how to create effective tables with specific constraints.
2. **Optimization of queries**: Use of indexes to improve the performance of queries.

## 📝 List of Tasks

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**We are all unique!**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/0-uniq_users.sql) | Create a `users` table with unique attributes. |
| 1 | [**In and not out**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/1-country_users.sql) | Create a `users` table with a country enumeration. |
| 2 | [**Best band ever!**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/2-fans.sql) | Ranking of the origins of metal bands by number of fans. |
| 3 | [**Old school band**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/3-glam_rock.sql) | List Glam rock bands by longevity. |
| 4 | [**Buy buy buy**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/4-store.sql) | Create a trigger that decreases the quantity of an item after adding an order. |
| 5 | [**Email validation to sent**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/5-valid_email.sql) | Create a trigger resetting the 'valid_email' attribute only if the email is modified. |
| 6 | [**Add bonus**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/6-bonus.sql) | Create a stored `AddBonus` procedure to add a new correction for a student. |
| 7 | [**Average score**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/7-average_score.sql) | Create a stored procedure `ComputeAverageScoreForUser` calculating and storing the average of a student's scores. |
| 8 | [**Optimize simple search**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/8-index_my_names.sql) | Create an index on the first name and the first letter of the name in the `names` table. |
| 9 | [**Optimize search and score**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/9-index_name_score.sql) | Create an index on the first name, the first letter of the name and the score in the `names` table. |
| 10 | [**Safe divide**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/10-div.sql) | Create a `SafeDiv` function dividing the first number by the second or returning 0 if the second number is 0. |
| 11 | [**No table for a meeting**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/11-need_meeting.sql) | Create a `need_meeting` view listing students with a score below 80 and not having a `last_meeting` or having one over a month ago. |
| 12 | [**Average weighted score**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/100-average_weighted_score.sql) | Create a procedure `ComputeAverageWeightedScoreForUser` for calculating a student's weighted average score. |
| 13 | [**Average weighted score for all!**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/MySQL_Advanced/101-average_weighted_score.sql) | Create a procedure `ComputeAverageWeightedScoreForUsers` for calculating weighted averages for all students. |


## 📬 Contact
- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
