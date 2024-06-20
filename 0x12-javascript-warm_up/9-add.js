#!/usr/bin/node
// add
const firstInt = parseInt(process.argv[2]);
const secInt = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}
if (isNaN(firstInt) || isNaN(secInt)) {
  console.log('NaN');
} else {
  console.log(add(firstInt, secInt));
}
