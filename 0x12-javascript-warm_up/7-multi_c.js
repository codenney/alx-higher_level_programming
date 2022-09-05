#!/usr/bin/node
// A script that prints x times “C is fun”

const argvInt = parseInt(process.argv[2]);

if (argvInt) {
  for (let i = 0; i < argvInt; i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
