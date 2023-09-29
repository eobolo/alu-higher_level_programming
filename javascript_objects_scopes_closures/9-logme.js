#!/usr/bin/node
class Calls {
  static number = -1;
  constructor () {
    Calls.number++;
  }

  call () {
    return Calls.number;
  }
}
exports.logMe = function (item) {
  const count = new Calls().call();
  console.log(`${count}: ${item}`);
};
