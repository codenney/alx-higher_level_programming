#!/usr/bin/node
// A function that increments and calls a function

const addMeMaybe = (num, func) => {
  func((num += 1));
};
module.exports = { addMeMaybe };
