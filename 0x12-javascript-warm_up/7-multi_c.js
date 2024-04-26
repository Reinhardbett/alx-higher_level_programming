#!/usr/bin/node

const args = require('process').argv;

for (let i = 0; i < Number(args[2]); i++) {
  console.log('C is fun');
}
if (!args[2]) {
  console.log('Missing number of occurrences');
}
