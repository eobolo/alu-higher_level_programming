#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || h === undefined) {
      // This Block does nothing
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
module.exports = Rectangle;
