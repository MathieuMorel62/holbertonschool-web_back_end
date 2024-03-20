# <p align="center">Redis Basic</p>

## 📝 Description

Redis Basic is a project designed to offer a practical and fundamental understanding of Redis, a high-performance key-value database. The project covers the use of Redis for basic operations, its use as a simple cache, and implements various advanced features.

## 📚 Resources

- [Redis commands](https://redis.io/commands)
- [Redis python client](https://redis-py.readthedocs.io/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Install Redis on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)

## 🛠️ Technologies and Tools Used

- **Redis**: Used for in-memory data management, allowing fast and flexible operations.
- **Python**: Main programming language to interact with Redis.
- **Ubuntu 18.04**: Operating system on which the project is deployed and tested.

## 📋 Prerequisite

- `Python 3.7` or higher.
- `Redis server`: Installed on Ubuntu 18.04.

## 🚀 Installation and Configuration

1. Clone the repository: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Navigate to the project directory:

```sh
cd 0x0B_redis_basic
```

3. Install Redis on Ubuntu:

```sh
sudo apt-get -y install redis-server
```

4. Install the Redis client in Python:

```sh
pip3 install redis
```

5. Configure Redis to bind to the local IP address:

```sh
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

6. Start the Redis service:

```sh
service redis-server start
```

## ✨ Main Features

- **Channel storage in Redis**: Allows you to store and retrieve channels.
- **Reading data and recovering the original type**: Retrieves the data stored with its original type.
- **Value increment**: Allows you to automatically increment stored values.


## 📝 List of Tasks

0. [**Writing strings to Redis**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py): Implementation of the Cache class for string storage in Redis.
1. [**Reading from Redis and recovering original type**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py): Methods to read Redis data and retrieve their original type.
2. [**Incrementing values**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py): System for counting calls to Cache class methods.
3. [**Storing lists**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py): Storage of input and output histories for a function.
4. [**Retrieving lists**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py): Retrieving and displaying the call history of a function.
5. [**Implementing an expiring web cache and tracker**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/web.py): Implementation of an expiring web cache and a URL access tracking system.

## 📬 Contact

- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
