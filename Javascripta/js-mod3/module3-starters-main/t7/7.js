'use strict'
const trigger = document.getElementById('trigger');
const targetimage = document.getElementById('target');

trigger.addEventListener('mouseenter', function(){
 targetimage.src = 'img/picB.jpg';
});

trigger.addEventListener('mouseleave', () => {
  targetimage.src = 'img/picA.jpg';
});