#!/usr/bin/node
// square
const size = parseInt(process.argv[2]);

if (isNaN(size) || size < 1) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) { console.log('X'.repeat(size)); }
}
