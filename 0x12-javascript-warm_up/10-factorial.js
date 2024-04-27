#!/usr/bin/node

const args = require('process').argv;

function factorialRecursive (n) {
  if (n === 0 || isNaN(Number(n))) {
    return (1);
  } else {
    return (n * factorialRecursive(n - 1));
  }
}

console.log(factorialRecursive(args[2]));
