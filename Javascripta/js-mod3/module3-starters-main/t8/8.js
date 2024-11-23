'use strict'
let calculation = 0

document.getElementById('start').addEventListener('click', function() {
  const num1 = document.getElementById('num1').value;
  const num2 = document.getElementById('num2').value;
  const operation = document.getElementById('operation').value;
  const number1 = Number(num1)
  const number2 = Number(num2)
    if (operation === 'add'){
    calculation = number1 + number2;
  }else if (operation === 'sub'){
    calculation = number1 - number2;
  }else if (operation === 'multi'){
    calculation = number1 * number2;
  }else if (operation ==='div'){
    calculation = number1 / number2;
  }
    const result = document.getElementById('result')
    result.innerHTML = ("The result is: " + calculation)
})

