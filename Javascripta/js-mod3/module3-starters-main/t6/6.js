'use strict'

const button = document.querySelector('button');
  button.addEventListener('click', function(evt){
    //jekkupekku
  for (let i = 0; i < 5; i++) {
    alert('element ' + evt.currentTarget.tagName + 'was clicked!!!!')
  }
});
