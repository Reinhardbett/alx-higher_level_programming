#!/usr/bin/node

const args = require('process').argv.slice(2);

if (args.length === 1 || !args[0]) {
  console.log(0);
} else {
  // sort new array in descending manner
  args.sort((a, b) => b - a);
  console.log(`${args[1]}`);
}
