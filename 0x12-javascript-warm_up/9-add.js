#!/usr/bin/node

const args = require('process').argv;

function add (a, b) {
  return (a + b);
}

const a = Number(args[2]);
const b = Number(args[3]);

console.log(add(a, b));
