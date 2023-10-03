#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

if (argv[2]) {
  const options = {
    method: 'GET',
    uri: argv[2]
  };
  request(argv[2], options, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const id = 18;
    request(JSON.parse(body).results[0].characters[id - 3], (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log(JSON.parse(body).films.length);
    });
  });
} else {
  console.log('An error occured missing url command line arg.');
}
