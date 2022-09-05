#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments

const argvArry = process.argv;
if (argvArry.length < 4) console.log(0);
else {
  const newArr = argvArry.slice(2).sort((a, b) => b - a);
  console.log(newArr[1]);
}
