#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

request(argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const objects = {};
  data.forEach(function (element, index, array) {
    const userId = element.userId;
    const completed = element.completed;
    if (this[`${userId}`] === undefined) {
      if (!completed) {
        //Do nothing
      } else {
        this[`${userId}`] = 1;
      }
    } else {
      if (!completed) {
        //Do nothing
      } else {
        this[`${userId}`]++;
      }
    }
  }, objects);
  console.log(objects);
});
