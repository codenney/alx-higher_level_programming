#!/usr/bin/node
// A function that executes x times a function

const callMeMoby = (x, func) => {
  for (let i = 0; i < x; i++) func();
};
module.exports = { callMeMoby };
