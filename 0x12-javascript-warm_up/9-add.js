#!/usr/bin/node
// A script that prints the addition of 2 integers

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const add = (a, b) => {
  return a + b;
};
console.log(add(a, b));
