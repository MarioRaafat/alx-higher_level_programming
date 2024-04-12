#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint(c = 'X') {
    for (let i = 0; i < this.height; i++) {
      const s = c.repeat(this.width);
      console.log(s);
  }
}
module.exports = Square;
