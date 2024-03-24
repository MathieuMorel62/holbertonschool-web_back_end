export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // Overload of conversion into numbers
  valueOf() {
    return this._size;
  }

  // Overload of conversion into strings
  toString() {
    return this._location;
  }
}
