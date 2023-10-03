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
    try {
      const parsedData = JSON.parse(body);
      const url = parsedData.results[0].characters[id - 3];
      request(url, (err, response, body) => {
        if (err) {
          console.log(err);
          return;
        }
        console.log(JSON.parse(body).films.length);
      });
    } catch (error) {
      console.log(error);
    }
  });
} else {
  console.log('An error occured missing url command line arg.');
}
