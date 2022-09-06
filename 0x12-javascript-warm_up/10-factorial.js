#!/usr/bin/node
// A script that computes and prints a factorial

const num = parseInt(process.argv[2]);
const factor = (n) => {
  if (!n) return 1;
  else if (n < 0 || n === 1) return 1;
  else return n * factor(n - 1);
};
console.log(factor(num));
