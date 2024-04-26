#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const newList = list.filter(n => n === searchElement);
  return (newList.length);
};
