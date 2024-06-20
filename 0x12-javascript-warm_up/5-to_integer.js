#!/usr/bin/node
// first argument num
const firstArg = parseInt(process.argv[2]);

if (!isNaN(firstArg)) {
  console.log('My number:', firstArg);
} else {
  console.log('Not a number');
}
