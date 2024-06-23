#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

function newProperty () {
  return (myObject.value += 1);
}

myObject.incr = newProperty;

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
