#!/usr/bin/node
// args count
const args = process.argv.length - 2;

// print a message
if (args === 0) {
  console.log('No argument');
} else if (args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
