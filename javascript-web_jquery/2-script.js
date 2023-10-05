#!/usr/bin/node
const divId = document.querySelector('DIV#red_header');
const header = document.querySelector('header');
divId.addEventListener('click', (event) => {
  header.style.color = '#FF0000';
});
