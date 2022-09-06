#!/usr/bin/node
// A script that computes and prints a factorial

const num = process.argv[2];

const factorial = (num) => {
  if (!num) return 1;
  else if (num < 0 || num === 1) return 1;
  else return num * factorial(num - 1);
};
console.log(factorial(num));
