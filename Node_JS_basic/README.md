# <p align="center">Node JS Basic</p>

![nodejs](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/c26fa56b-88d4-4e18-8895-e9a943094be9)

## 📝 Description

This project aims to initiate the basics of NodeJS. It covers the execution of JavaScript with NodeJS, the use of NodeJS modules, the creation of HTTP servers with NodeJS and Express, and the organization of complex HTTP servers with Express. Learning objectives include understanding NodeJS modules, managing files and command line arguments, and creating basic and advanced HTTP servers.

## 📚 Resources

- [Node JS getting started](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs)
- [Process API doc](https://node.readthedocs.io/en/latest/api/process/)
- [Child Process](https://nodejs.org/api/child_process.html)
- [Express getting started](https://expressjs.com/fr/starter/installing.html)
- [Mocha documentation](https://mochajs.org/)
- [Nodemon documentation](https://www.npmjs.com/package/nodemon)

## 🛠️ Technologies and Tools Used

- **Node.js**: Used to run JavaScript on the server.
- **Express.js**: Framework for creating HTTP servers.
- **Mocha**: Test framework for Node.js applications.
- **Nodemon**: Tool to develop Node.js applications by automatically reloading the server.

## 📊 Data Files

<details>
  <summary>database.csv</summary>
  <br>

  ```csv
firstname,lastname,age,field
Johann,Kerbrou,30,CS
Guillaume,Salou,30,SWE
Arielle,Salou,20,CS
Jonathan,Benou,30,CS
Emmanuel,Turlou,40,CS
Guillaume,Plessous,35,CS
Joseph,Crisou,34,SWE
Paul,Schneider,60,SWE
Tommy,Schoul,32,SWE
Katie,Shirou,21,CS
```

</details>
<details>
  <summary>package.json</summary>
  <br>

  ```json
{
  "name": "node_js_basics",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "test": "./node_modules/mocha/bin/mocha --require babel-register --exit",
    "dev": "nodemon --exec babel-node --presets babel-preset-env ./server.js ./database.csv"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "chai-http": "^4.3.0",
    "express": "^4.17.1"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "nodemon": "^2.0.2",
    "eslint": "^6.4.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-plugin-import": "^2.18.2",
    "eslint-plugin-jest": "^22.17.0",
    "chai": "^4.2.0",
    "mocha": "^6.2.2",
    "request": "^2.88.0",
    "sinon": "^7.5.0"
  }
}
```

</details>
<details>
  <summary>babel.config.js</summary>
  <br>

  ```javascript
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
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
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

1. Clone the directory: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end.git
```

2. Go to the project file: 

```sh
cd Node_JS_basic
```

3. Install the dependencies:

```sh
npm install
```

4. Run the server:

```sh
npm run dev
```

## 💡 Use

- Run Node.js scripts with the command `node <file-name.js>`.
- Use `npm run test` to run the tests.

## ✨ Main Features

1. **Executing JavaScript scripts**: Using Node.js to execute server-side JavaScript scripts.
2. **HTTP server creation**: Using Node.js and Express to create HTTP servers.
3. **Data management**: Reading and managing data from CSV files.

## 📝 List of Tasks

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**Executing basic javascript with Node JS**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/0-console.js) | Create a function to display standard output messages. |
| 1 | [**Using Process stdin**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/1-stdin.js) | Create a program to read user entries. |
| 2 | [**Reading a file synchronously with Node JS**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/2-read_file.js) | Use a CSV database and create a function to count students. |
| 3 | [**Reading a file asynchronously with Node JS**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/3-read_file_async.js) | Same task as the previous one, but reading the file asynchronously. |
| 4 | [**Create a small HTTP server using Node's HTTP module**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/4-http.js) | Use the http module to create a simple HTTP server. |
| 5 | [**Create a more complex HTTP server using Node's HTTP module**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/5-http.js) | Create an HTTP server displaying student information. |
| 6 | [**Create a small HTTP server using Express**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/6-http_express.js) | Install Express and create an HTTP server. |
| 7 | [**Create a more complex HTTP server using Express**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/7-http_express.js) | Use Express to create a server with advanced routes. |
| 8 | [**Organize a complex HTTP server using Express**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/Node_JS_basic/full_server) | Structure a complete server with controllers, routes and utilities. |

## 📬 Contact
- Profil LinkedIn : [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
