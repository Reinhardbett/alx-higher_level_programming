#!/usr/bin/node
// Print the first argument passed to stdout

// Include the process module
const process = require('process');

// Print the first argument
if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
