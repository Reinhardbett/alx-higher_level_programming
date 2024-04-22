#!/usr/bin/node
// Print a message depending on number of arguments

// Include process module
const process = require('process');

// Print message depending on argv elements
const args = process.argv;
if (args.length === 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
