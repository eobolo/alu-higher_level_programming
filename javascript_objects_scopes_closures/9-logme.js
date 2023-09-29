#!/usr/bin/node
class Calls {
  constructor () {
    Calls.number++;
  }

  static number = -1;
  call () {
    return Calls.number;
  }
}
exports.logMe = function (item) {
  const count = new Calls().call();
  console.log(`${count}: ${item}`);
};
