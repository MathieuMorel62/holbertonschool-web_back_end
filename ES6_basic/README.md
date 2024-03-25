# <p align='center'>ES6 Basics</p>

![ES6](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/5410e72b-6d8e-4ae1-b7ef-d9868479ac08)

## 📝 Description
The **ES6 Basics** project is an in-depth exploration of the features of ECMAScript 6, offering an overview of the new features and improvements made to the JavaScript language. This project covers key concepts such as const and let variables, arrow functions, default settings, spread and rest operators, as well as new methods for strings and objects.

## 📚 Resources
- [ECMAScript 6 - ECMAScript 2015](https://www.w3schools.com/js/js_es6.asp)
- [Statements and declarations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements)
- [Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [Default parameters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters)
- [Rest parameter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)
- [Javascript ES6 — Iterables and Iterators](https://towardsdatascience.com/javascript-es6-iterables-and-iterators-de18b54f4d4)

## 🛠️ Technologies and Tools Used

- **JavaScript ES6**: Programming language used to explore new features.
- **Node.js**: Execution environment to execute JavaScript code outside the browser.
- **Jest**: Test framework to validate JavaScript code.
- **Babel**: Transcompiler to write modern JavaScript code and convert it into a version compatible with current browsers.
- **ESLint**: Linting tool to maintain the quality of the code.

## 📋 Prerequisite

- Node.js version 12.11.x or higher
- npm (Node Package Manager)
- Specific configurations listed in the file `package.json`

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

1. Clone the repository: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/ES6_basic
```

2. Install the dependencies: 

```sh
npm install
```

3. Run the tests: 

```sh
npm run test
```

## 💡 Use
- Run specific scripts to see the features of ES6 in action.
- Explore code examples to understand the application of new syntaxes and features.

## ✨ Main Features
1. **Const and let variables**: Understand the scope and use of new variable declarations.
2. **Arrow functions**: Concise syntax for writing functions.
3. **Default settings and spread/rest operators**: Modern techniques for managing function parameters.
4. **String templates**: Effective use of template literals for strings.
5. **Object literals**: Simplified syntax for creating objects.
6. **Destructuring**: Extracting values from arrays and objects.
7. **Iterables and iterators**: Understanding the concepts of iterables and iterators in ES6.

## 📝 List of Tasks

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**Const or let?**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/0-constants.js) | Modify the code to correctly use const and let. |
| 1 | [**Block Scope**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/1-block-scoped.js) | Use block scope with new variable declarations. |
| 2 | [**Arrow functions**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/2-arrow.js) | Rewrite functions using arrow function syntax. |
| 3 | [**Parameter defaults**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/3-default-parameter.js) | Simplify functions using default parameters. |
| 4 | [**Rest parameter syntax for functions**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/4-rest-parameter.js) | Use the rest parameter syntax for managing function arguments. |
| 5 | [**The wonders of spread syntax**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/5-spread-operator.js) | Utilize the spread syntax to merge arrays and strings. |
| 6 | [**Take advantage of template literals**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/6-string-interpolation.js) | Use template literals to enhance string concatenation. |
| 7 | [**Object property value shorthand syntax**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/7-getBudgetObject.js) | Simplify object creation with shorthand syntax for properties. |
| 8 | [**No need to create empty objects before adding properties**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/8-getBudgetCurrentYear.js) | Dynamically add properties to objects using computed property names. |
| 9 | [**ES6 method properties**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/9-getFullBudget.js) | Employ ES6 method property syntax in objects. |
| 10 | [**For...of Loops**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/10-loops.js) | Utilize the for...of loop to iterate over array elements. |
| 11 | [**Iterator**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/11-createEmployeesObject.js) | Create custom objects with iterator methods. |
| 12 | [**Let's create a report object**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/12-createReportObject.js) | Construct a complex report object. |
| 13 | [**Iterating through report objects**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/100-createIteratorObject.js) | Iterate through object properties and values. |
| 14 | [**Iterate through object**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_basic/101-iterateThroughObject.js) | Navigate objects using iteration to generate formatted strings. |

## 📬 Contact
- Profil LinkedIn: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
