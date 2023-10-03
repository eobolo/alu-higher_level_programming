#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
const fs = require('fs');
/*
 Using a file stream
*/
request(argv['2']).pipe(fs.createWriteStream(argv[3]));
