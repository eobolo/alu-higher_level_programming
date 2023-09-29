#!/usr/bin/node
exports.logMe = function (item) {
  const pathName = 'Loggings.txt';
  const fs = require('fs');
  const readData = parseInt(readFromFile(pathName, fs));
  console.log(`${readData}: ${item}`);
  const writeData = readData + 1;
  writeToFile(pathName, writeData.toString(), fs);
};

function readFromFile (pathName, fs) {
  let data;
  try {
    data = fs.readFileSync(pathName, 'utf-8');
    return data;
  } catch (err) {
    data = 0;
    return data;
  }
}

function writeToFile (pathName, dataToWrite, fs) {
  try {
    fs.writeFileSync(pathName, dataToWrite, 'utf-8');
    return 0;
  } catch (err) {
    // do nothing
    return 1;
  }
}
