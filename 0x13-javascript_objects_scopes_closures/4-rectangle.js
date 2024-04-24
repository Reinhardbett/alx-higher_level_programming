#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
  }

  // Same as [this.width,...] = [this.height, ...]
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Destructuring instance properties in arrays
  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
};
