#!/usr/bin/node
const args = require('process').argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
