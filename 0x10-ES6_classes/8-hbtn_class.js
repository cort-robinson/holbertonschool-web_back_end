export default class HolbertonClass {
  constructor(size, location) {
    if (typeof size === 'number') {
      this._size = size;
    }
    if (typeof location === 'string') {
      this._location = location;
    }
  }

  valueOf() {
    return this._size;
  }

  toString() {
    return this._location;
  }
}
