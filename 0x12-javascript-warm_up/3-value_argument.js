#!/usr/bin/node
// A script that prints the first argument passed to it

const firstArgv = process.argv[2];
if (firstArgv === undefined) console.log('No argument');
else console.log(firstArgv);
