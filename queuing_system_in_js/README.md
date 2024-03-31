# <p align="center">Queuing System In JS</p>

![queuing](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/34a3e45a-9dae-4134-b36a-fc2009216cc8)

## 📝 Description
This project implements a queuing system using JavaScript and Redis. It is designed to manage tasks in a queue, offering efficient handling of workloads. The system demonstrates the use of Redis as a database and message broker, and includes key features like job creation and processing, progress tracking, and error handling.

## 📚 Resources
- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis Client Interface](https://redis.io/docs/connect/cli/)
- [Redis client for Node JS](https://github.com/redis/node-redis)
- [Using Kue for job queues](https://github.com/Automattic/kue)

## 🛠️ Technologies and Tools Used
- **JavaScript (Node.js)**: Core programming language.
- **Redis**: Used for managing job queues and caching.
- **Kue**: A priority job queue backed by Redis.
- **Express.js**: Used for implementing the server for job management.
- **Docker**: Used for containerization of the application.

## 📋 Prerequisites
- Node.js version 12.x or higher.
- Redis server version 5.0.7 or higher.
- Knowledge of JavaScript and asynchronous programming in Node.js.

## 📊 Data Files

<details>
<summary>package.json</summary>
<br>

```json
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
```

</details>
<details>
<summary>.babelrc</summary>
<br>

```json
{
  "presets": [
    "@babel/preset-env"
  ]
}
```

</details>

## 🚀 Installation

1. Clone the repository.

```bash
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Change the directory.

```bash
cd queuing_system_in_js
```

3. Install the dependencies.

```bash
npm install
```

4. Start the server.

```bash
npm run dev 
```

## 💡 Usage
- **Job Creation**: Create jobs to be processed with specific attributes like phone number and message.
- **Job Processing**: Jobs are processed in the order they are queued with status updates.
- **Monitoring**: The system monitors job status, showing completion, progress, or failure.
- **Error Handling**: Errors are handled gracefully, with failed jobs being retried or moved to a failed queue.

## ✨ Main Features
1. **Job Queuing**: Dynamically queue jobs and manage workload.
2. **Real-time Monitoring**: Track job status in real-time.
3. **Scalability**: Designed to scale with increasing workload.

## 📝 Task List

| Number | Task                                  | Description                                                    |
| ------ | ------------------------------------- | -------------------------------------------------------------- |
| 0      | [**Install a redis instance**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/0-redis_client.js) | Set up and start Redis server.                                  |
| 1      | [**Node Redis Client**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/1-redis_op.js) | Connect to Redis with Node.js.                                  |
| 2      | [**Node Redis client and basic operations**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/1-redis_op.js) | Basic operations with Redis and Node.js.                        |
| 3      | [**Node Redis client and async operations**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/2-redis_op_async.js) | Implement async operations with Redis and Node.js.              |
| 4      | [**Node Redis client and advanced operations**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/4-redis_advanced_op.js) | Advanced operations with Redis client.                          |
| 5      | [**Node Redis client publisher and subscriber**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/5-subscriber.js) | Implement publisher and subscriber with Redis in Node.js.       |
| 6      | [**Create the Job creator**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/6-job_creator.js) | Set up job creation functionality using Kue.                    |
| 7      | [**Create the Job processor**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/6-job_processor.js) | Develop job processing functionality using Kue.                |
| 8      | [**Track progress and errors with Kue: Create the Job creator**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/7-job_creator.js) | Track job progress and handle errors.                           |
| 9      | [**Track progress and errors with Kue: Create the Job processor**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/7-job_processor.js) | Monitor job progress and errors.                                |
| 10     | [**Writing the job creation function**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/8-job.js) | Function for creating push notification jobs.                   |
| 11     | [**Writing the test for job creation**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/8-job.test.js) | Develop tests for job creation functionality.                   |
| 12     | [**In stock?**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/9-stock.js) | Implement inventory management features.                        |
| 13     | [**Can I have a seat?**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/queuing_system_in_js/100-seat.js) | Implement seat reservation system using Redis.                  |

## 📬 Contact
- LinkedIn Profile: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel62/)
