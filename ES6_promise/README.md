# <p align="center">ES6 Promise</p>

![es6](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/52dd5ced-41bb-479b-8caf-404080388ea5)

## 📝 Description
This project, entitled "ES6 Promises", is a set of practical exercises designed to deepen the understanding and application of the Promises in ES6 JavaScript. It aims to educate about the use of the methods `then`, `resolve`, `catch`, the `await` operator, and the creation of `async` functions. This project is essential for developers looking to master asynchronous operations in JavaScript.

## 📚 Resources
- [JavaScript Promise: An introduction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [Async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Throw/Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
- [ESLint - Pluggable JavaScript linter](https://eslint.org/)
- [Jest - Delightful JavaScript Testing](https://jestjs.io/)
- [Node.js](https://nodejs.org/)

## 🛠️ Technologies and Tools Used
- **Node.js**: Execution environment for server-side JavaScript.
- **Jest**: Test framework for JavaScript.
- **ESLint**: Linting tool for JavaScript.
- **Babel**: JavaScript transpilator to support the latest features of ES6.

## 📋 Prerequisite
- `NodeJS` version 12.11.x or newer.
- `NPM` (Node Package Manager) version 6.11.3 or newer.
- A text editor such as `Visual Studio Code`, `vim`, or `emacs`.

## 📊 Data Files

<details>
  <summary>package.json</summary>
  <br>

  ```json
  {
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "dev": "npx babel-node",
      "test": "jest",
      "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
    },
    "devDependencies": {
      "@babel/core": "^7.6.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.6.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "jest": "^24.9.0"
    }
  }
  ```

</details>
<details>
  <summary>babel.config.js</summary>
  <br>

  ```js
  module.exports = {
    presets: [
      [
        '@babel/preset-env',
        {
          targets: {
            node: 'current',
          },
        },
      ],
    ],
  };
  ```

</details>
<details>
  <summary>utils.js</summary>
  <br>

  ```js
  export function uploadPhoto() {
    return Promise.resolve({
      status: 200,
      body: 'photo-profile-1',
    });
  }
  
  
  export function createUser() {
    return Promise.resolve({
      firstName: 'Guillaume',
      lastName: 'Salva',
    });
  }
  ```

</details>
<details>
  <summary>.eslintrc.js</summary>
  <br>

  ```js
  module.exports = {
    env: {
      browser: false,
      es6: true,
      jest: true,
    },
    extends: [
      'airbnb-base',
      'plugin:jest/all',
    ],
    globals: {
      Atomics: 'readonly',
      SharedArrayBuffer: 'readonly',
    },
    parserOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
    },
    plugins: ['jest'],
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
    overrides:[
      {
        files: ['*.js'],
        excludedFiles: 'babel.config.js',
      }
    ]
  };
  ```

</details>

## 🚀 Installation and Configuration

1. Install NodeJS:

```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install -y nodejs
```
2. Verify the installation:

```bash
node -v
npm -v
```

3. Install Jest, Babel and ESLint in your project directory:

```bash
npm init -y
npm install --save-dev jest babel-jest @babel/core @babel/preset-env @babel/cli eslint
```

4. Clone the GitHub repository:

```bash
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

5. Navigate to the project directory:

```bash
cd ES6_promise
```

6. Install packages:

```sh
npm install
```

## 💡 Use
To run the tests of each task, use the following command in the project directory:

```bash
npm run test
```

## ✨ Main Features

- **Promise Management**: Understand and effectively use promises in JavaScript.
- **Async/Await**: Master asynchronous functions and the await operator for non-blocking operations.
- **Error management**: Use `try/catch` to manage errors in asynchronous operations.
- **ESLint**: Configure and use ESLint to maintain a clean and consistent codebase.
- **Jest**: Write and run tests using the Jest framework.

## 📝 Task List

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**Keep every promise you make and only make promises you can keep**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/0-promise.js) | Learn to create promises and understand their importance. |
| 1 | [**Don't make a promise...if you know you can't keep it**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/1-promise.js) | Manage the promises and their resolution or rejection according to the conditions. |
| 2 | [**Catch me if you can!**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/2-then.js) | Management of errors and rejections in promises. |
| 3 | [**Handle multiple successful promises**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/3-all.js) | Work with several promises and manage their collective resolution. |
| 4 | [**Simple promise**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/4-user-promise.js) | Create a simple promise returning a specific object. |
| 5 | [**Reject the promises**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/5-photo-reject.js) | Write functions that reject promises with errors. |
| 6 | [**Multiple handle promises**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/6-final-user.js) | Manage several promises and their states with `Promise.all`. |
| 7 | [**Load balancer**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/7-load_balancer.js) | Implement a load balancer using promises. |
| 8 | [**Throw an error**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/8-try.js) | Manage exceptions by throwing errors under certain conditions. |
| 9 | [**Throw error / try catch**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/9-try.js) | Use `try/catch` to manage errors in promises. |
| 10 | [**Await / Async**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_promise/100-await.js) | Use the `async` and `await` functions to simplify the processing of asynchronous operations. |

## 📬 Contact
- Profil LinkedIn: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
