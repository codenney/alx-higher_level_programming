#!/usr/bin/node
// A function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((el) => {
    el === searchElement && count++;
  });
  return count;
};
