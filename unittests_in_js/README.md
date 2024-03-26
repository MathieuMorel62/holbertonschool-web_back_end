# <p align="center">Unittests In JS</p>

📝 Description

The **Unittests in JS** project is an in-depth exploration of unit tests in JavaScript, using frameworks and tools such as `Mocha`, `Chai`, and `Sinon`. This project aims to teach good practices in unit testing, including how to write effective tests, use **spies**, **stubs**, and **hooks**, and perform integration tests.

## 📚 Resources

- [Mocha Documentation](https://mochajs.org/)
- [Documentation Chai](https://www.chaijs.com/)
- [Documentation Otherwise](https://sinonjs.org/)
- [How to Test NodeJS Apps using Mocha, Chai and SinonJS](https://www.digitalocean.com/community)
- [Request](https://www.npmjs.com/package/request)
- [ExpressJS Documentation](https://expressjs.com/)

## 🛠️ Technologies and Tools Used

- **Mocha and Chai**: Used to write and run unit tests.
- **Otherwise**: Allows the creation of spies, stubs, and mocks for tests.
- **Node.js**: Execution environment for server-side JavaScript.
- **Express.js**: Framework used to build web applications and APIs.

## 📋 Prerequisite

- **Node.js**: Version 12.x.x or higher.
- **NPM**: Package manager for JavaScript.

## 📊 Data Files

<details>
<summary>package.json</summary>
<br>

```json
{
  "name": "8-api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "./node_modules/mocha/bin/mocha"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}
```

</details>

## 🚀 Installation and Configuration

1. Clone the repository: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Navigate to the project folder: 

```sh
cd unittests_in_js/
```

3. Install the dependencies: 

```sh
npm install
```

4. Run the server:

```sh
node api.js
```

## 💡 Use

- Run `npm test` to launch all unit tests.
- Use `npm test <test_name>` to run a specific test.

## ✨ Main Features

1. **Basic Unit Tests**: Use of Mocha and Chai for the creation of simple and readable tests.
2. **Integration of Spies and Stubs**: Use of Otherwise to observe and modify the behavior of functions during tests.
3. **Asynchronous Tests**: Test support for asynchronous functions and API calls.

## 📝 Task List

| Number | Task | Test File | Description |
| ------ | ---- | ---- | ----------- |
| 0 | [**Basic test with Mocha and Node assertion library**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/0-calcul.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/0-calcul.test.js) | Installation and configuration of Mocha |
| 1 | [**Combining descriptions**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/1-calcul.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/1-calcul.test.js) | Improving tests with combined descriptions |
| 2 | [**Basic test using Chai assertion library**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/2-calcul_chai.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/2-calcul_chai.test.js) | Using Chai for more readable test syntax |
| 3 | [**Spies**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/utils.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/3-payment.test.js) | Using spies to monitor functions |
| 4 | [**Stubs**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/4-payment.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/4-payment.test.js) | Setting up stubs to simulate specific behaviors |
| 5 | [**Hooks**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/5-payment.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/5-payment.test.js) | Using hooks for test setup |
| 6 | [**Async tests with done**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/6-payment_token.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/6-payment_token.test.js) | Asynchronous tests with `done` callback |
| 7 | [**Skip**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/7-skip.test.js) | [Test File](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/unittests_in_js/7-skip.test.js) | Managing tests to be skipped |
| 8 | [**Basic Integration testing**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/unittests_in_js/8-api) | [API Tests](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/unittests_in_js/8-api) | Integration testing for an API |
| 9 | [**Regex integration testing**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/unittests_in_js/9-api) | [API Tests](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/unittests_in_js/9-api) | Integration testing with regex validation |
| 10 | [**Deep equality & Post integration testing**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/unittests_in_js/10-api) | [API Tests](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/unittests_in_js/10-api) | Deep equality testing and POST method tests |


## 📬 Contact

- Profil LinkedIn : [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-913b4a62)
