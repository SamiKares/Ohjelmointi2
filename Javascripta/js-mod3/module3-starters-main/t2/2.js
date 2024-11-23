'use strict'
const targetElement = document.getElementById('target');

const First = document.createElement('li');
First.textContent = 'First item';
targetElement.appendChild(First);

const second = document.createElement('li');
second.textContent = 'Second item';
second.classList.add('my-item');
targetElement.appendChild(second);

const third = document.createElement('li');
third.textContent = 'Third item';
targetElement.appendChild(third);
