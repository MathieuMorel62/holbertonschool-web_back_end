# <p align="center">ES6 Data Manipulation</p>

![data](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/2f434462-5461-4ff3-9e1d-9d94bbea373a)

## 📝 Description

This project focuses on data manipulation using the features of ES6. It explores advanced array manipulation techniques, the use of Typed Arrays, and the implementation of data structures such as Set, Map, and WeakMap. This project is intended to strengthen ES6 skills and to understand in depth the common data operations in web development.

## 📚 Resources

- [ES6 documentation](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes)
- [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Typed Arrays in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Typed_arrays)
- [Use Set in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
- [Map and WeakMap manipulation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- [Unit tests with Jest](https://jestjs.io/)

## 🛠️ Technologies and Tools Used

- **JavaScript ES6**: Main programming language.
- **Node.js**: Execution environment.
- **Jest**: For unit tests.
- **Babel**: Transcompiler for JavaScript.
- **ESLint**: Linter to maintain a clean code that complies with standards.

## 📋 Prerequisite

- Node.js v12.11.1
- npm v6.11.3
- A code editor such as Visual Studio Code or Vim.

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

1. Clone the repository from [GitHub](https://github.com/MathieuMorel62/holbertonschool-web_back_end/tree/main/ES6_data_manipulation).
2. Install `Node.js` and `npm` if you have not already done so.
3. At the root of the project, run `npm install` to install the dependencies.
4. To run the tests, use the `npm run test` command.

## 💡 Use

- Run individual JavaScript scripts to see data manipulation in action.
- Use the functions provided to process and manipulate your own data.

## ✨ Main Features

1. **Array manipulation**: Use of methods such as map, filter, and reduce.
2. **Typed Arrays**: Efficient management of binary data.
3. **Data Structures**: Implementation of Set, Map, and WeakMap for advanced use cases.

## 📝 List of Tasks

| Number | Task | Description |
| ------ | ---- | ----------- |
| 0 | [**Basic list of objects**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/0-get_list_students.js) | Create a list of students as an object. |
| 1 | [**More mapping**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/1-get_list_student_ids.js) | Manipulation of student identifiers. |
| 2 | [**Filter**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/2-get_students_by_loc.js) | Filter students by location. |
| 3 | [**Reduce**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/3-get_ids_sum.js) | Calculate the sum of student identifiers. |
| 4 | [**Combine**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/4-update_grade_by_city.js) | Update student notes by city. |
| 5 | [**Typed Arrays**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/5-typed_arrays.js) | Creating an ArrayBuffer with a specific Int8 value. |
| 6 | [**Set data structure**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/6-set.js) | Creating a Set from an array. |
| 7 | [**More set data structure**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/7-has_array_values.js) | Checking for the presence of values from an array in a Set. |
| 8 | [**Clean set**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/8-clean_set.js) | Clean a Set according to a specific string. |
| 9 | [**Map data structure**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/9-groceries_list.js) | Creating a shopping list with Map. |
| 10 | [**More map data structure**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/10-update_uniq_items.js) | Update of unique elements in a Map. |
| 11 | [**Weak link data structure**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_data_manipulation/100-weak.js) | Management of API requests with WeakMap. |

## 📬 Contact
- Profil LinkedIn : [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
