# <p align="center">ES6 Classes</p>

![classe](https://github.com/MathieuMorel62/holbertonschool-web_back_end/assets/113856302/870d1321-10fe-4b31-9c03-715d222b1ba7)

## 📝 Description

This **ES6 Classes** project is designed to explore and implement advanced concepts of object-oriented programming in ES6 JavaScript. It covers topics such as class definition, addition of methods, use of static methods, inheritance, and metaprogramming techniques.

## 📚 Resources

- [JavaScript Classes](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Classes)
- [Metaprogramming](https://www.keithcirkel.co.uk/metaprogramming-in-es6-symbols/#symbolspecies)
- [ES6 in detail](https://exploringjs.com/es6/index.html)
- [Jest](https://jestjs.io/)
- [Babel](https://babeljs.io/)
- [ESLint](https://eslint.org/)

## 🛠️ Technologies and Tools Used

- **JavaScript ES6**: To take advantage of the new features of ES6.
- **Node.js**: Execution environment for JavaScript.
- **Jest**: For unit tests.
- **Babel**: Transcompiler to ensure code compatibility.
- **ESLint**: To ensure compliance and quality of the code.

## 📋 Prerequisite

- `NodeJS` version 12.11.x
- `npm` version 6.11.3
- `Jest`, `Babel`, `ESLint` (dependencies installed via npm)

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
    "@babel/preset-env": "^7.6.0",
    "@babel/node": "^7.8.0",
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

1. Clone the repository: 

```sh
git clone https://github.com/MathieuMorel62/holbertonschool-web_back_end/
```

2. Navigate to the project folder: 

```sh
cd ES6_classes
```

3. Install the dependencies: 

```sh
npm install
```

4. Run the tests: 

```sh
npm run test
```

## 💡 Use

To launch the demo scripts, use `npm run dev <script_name.js>`. For example:

```bash
npm run dev 0-main.js
```

## 📝 List of Tasks

| Number | Task | Description |
| ------ | ----- | ----------- |
| 0 | [**ClassRoom**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/0-classroom.js) | Implementation of a simple class with a `_maxStudentsSize` attribute. |
| 1 | [**Room Initialization**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/1-make_classrooms.js) | Creation of an array of ClassRoom objects with predefined sizes. |
| 2 | [**HolbertonCourse Getters/Setters**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/2-hbtn_course.js) | Management of the properties of a course with accessors and mutators. |
| 3 | [**Currency**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/3-currency.js) | Class with methods to display the currency. |
| 4 | [**Pricing**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/4-pricing.js) | Class integrating Currency to manage prices. |
| 5 | [**Building Abstract Class**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/5-building.js) | Creation of an abstract class with an evacuation method to overload. |
| 6 | [**SkyHighBuilding**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/6-sky_high.js) | Class inherited from Building with additional features for high-rise buildings. |
| 7 | [**Airport**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/7-airport.js) | Class representing an airport with custom methods. |
| 8 | [**HolbertonClass**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/8-hbtn_class.js) | Class with special conversion methods for size and location. |
| 9 | [**Hoisting**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/9-hoisting.js) | Solving hoisting problems in ES6. |
| 10 | [**Car**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/10-car.js) | Basic class representing a car with a cloning method. |
| 11 | [**EVCar**](https://github.com/MathieuMorel62/holbertonschool-web_back_end/blob/main/ES6_classes/100-evcar.js) | Extension of the Car class specific to electric cars. |

## 📬 Contact
- Profil LinkedIn: [Mathieu Morel](https://www.linkedin.com/in/mathieu-morel-9ab457261/)
