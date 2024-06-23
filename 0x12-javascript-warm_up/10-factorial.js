#!/usr/bin/node
const args = require('process').argv;

// create function to compute factorial of input
function factorial (n) {
  if (n < 0) {
    return (undefined);
  }
  if (n === 0 || n === 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}

// check if input is NaN before printing factorial
if (isNaN(Number(args[2]))) {
  console.log(1);
} else {
  console.log(factorial(Number(args[2])));
}
