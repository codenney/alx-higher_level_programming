#!/usr/bin/node
// A script that prints something if the first argument can be converted to an integer

const convertNum = parseInt(process.argv[2]);
if (convertNum) console.log(`My number: ${convertNum}`);
else console.log(`Not a number`);
