'use strict';
const names = ['John', 'Paul', 'Jones'];

const targetElement = document.getElementById('target');

let htmllist = '';

for (const name of names) {
  htmllist += `<li>${name}</li>`;
}
targetElement.innerHTML = htmllist;