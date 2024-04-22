#!/usr/bin/node
// Concatenate and print two stdout arguments

// Include the process module
const process = require('process');

// Print arguments in a concatenated string
console.log(`${process.argv[2]}` + ' is ' + `${process.argv[3]}`);
