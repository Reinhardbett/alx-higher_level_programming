#!/usr/bin/node

const args = require('process').argv;

if (!args[2] || isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(args[2]); i++) {
    console.log('X'.repeat(args[2]));
  }
}
