# <p align="center">Redis Basic</p>

![redis](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/54f5a93d-528a-4842-ac06-2aae3c08e39a)

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

## 💡 Use

<details>
  <summary>Main test</summary>
  <br>

  ```python
  #!/usr/bin/env python3
"""
Main file test 1
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))




""" Main file test 2"""

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))



""" Main file test 3 """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
```

</details>

- Run the main script: `python main.py`
- Use the functions defined in `exercise.py` to interact with Redis.

## ✨ Main Features

- **Channel storage in Redis**: Allows you to store and retrieve channels.
- **Reading data and recovering the original type**: Retrieves the data stored with its original type.
- **Value increment**: Allows you to automatically increment stored values.


## 📝 List of Tasks

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**Writing strings to Redis**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py) | Implementation of the Cache class for storing strings in Redis. |
| 1 | [**Reading from Redis and recovering original type**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py) | Methods to read data from Redis and retrieve their original types. |
| 2 | [**Incrementing values**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py) | System for incrementing the count of calls to Cache class methods. |
| 3 | [**Storing lists**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py) | Storage of input and output histories for a particular function. |
| 4 | [**Retrieving lists**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/exercise.py) | Methods for retrieving and displaying the call history of a function. |
| 5 | [**Implementing an expiring web cache and tracker**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/0x0B_redis_basic/web.py) | Implementation of an expiring web cache and a system for tracking URL accesses. |

## 📬 Contact

- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
