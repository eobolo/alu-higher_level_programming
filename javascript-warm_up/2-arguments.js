#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 2) {
  console.log('No arguement');
} else if (argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguements found');
}
