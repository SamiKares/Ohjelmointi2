'use strict';

// tehtävä 1 //
console.log("I'm printing to console!")

//tehtävä 2 //
const nimi = prompt('Mikä sinun nimesi on?')
console.log(`${nimi}`)

// tehtävä 3 //
let numero1 = Number(prompt('Anna ensimmäinen numero.'))
let numero2 = Number(prompt('Anna toinen numero.'))
let numero3 = Number(prompt('Anna numero kolme.'))
let summa = parseInt(numero1 + numero2 + numero3)
let keskiarvo = parseInt(summa / 3)
console.log(summa)
console.log(keskiarvo)
document.querySelector('#laskin').innerHTML = 'Lukujen summa on: ' + summa;
document.querySelector('#keskiarvo').innerHTML = 'Lukujen keskiarvo on: ' +
    keskiarvo;
document.querySelector('#tervehdys').innerHTML = 'Hello!, ' + nimi + '!';

// tehtävä 4//
let tupa;
const harrypotter = Math.random();
if (harrypotter < 0.25) {
  tupa = "Gryffindor"
} else if (harrypotter > 0.25 && harrypotter < 0.5) {
  tupa = "Slytherin"
} else if (harrypotter > 0.5 && harrypotter < 0.75) {
  tupa = "Hufflepuff"
} else if (harrypotter > 0.75) {
  tupa = "Ravenclaw"
}
document.querySelector('#harrypotter').innerHTML = nimi + ', You are a: ' +
    tupa;
let vastaus

//tehtävä 5
const vuosi = prompt('Anna vuosiluku niin kerron sinulle onko se karkausvuosi');
const vuosiluku = parseInt(vuosi)
if (vuosiluku % 4 === 0 && vuosiluku % 100 !== 0 || vuosiluku % 400 === 0) {
  vastaus = vuosiluku + " on karkausvuosi";
} else {
  vastaus = vuosiluku + " ei ole karkausvuosi";
}
document.querySelector('#karkaus').innerHTML = vastaus;


// tehtävä 6
let squarerooter = confirm('Should i calculate the squareroot?');
console.log(squarerooter);
let vastaussquare;
let squarerootcalc;
if (squarerooter === false) {
  vastaussquare = "The square root is not calculated."
} else {
  squarerootcalc = prompt('Anna numero')
  const juuri = parseFloat(squarerootcalc)
  if (juuri <= 0) {
    vastaussquare = 'The square root of a negative number is not defined'
  } else {
    vastaussquare = `The squareroot of  ${juuri} is ${Math.sqrt(
        squarerootcalc)}`
  }
}
document.querySelector('#square').innerHTML = vastaussquare;

// tehtävä 7
let diceresult;
let howmanytrhows;
let diceamount;
let thrownumber = 0;
const dicesum = [];

howmanytrhows = prompt('Montako kertaa noppaa heitetään?');
diceamount = parseInt(howmanytrhows);

do {
  diceresult = Math.floor(Math.random() * 6) + 1;
  thrownumber++;
  dicesum.push(diceresult);
} while (thrownumber < diceamount);
console.log("Yksittäiset heitot", dicesum)

let totalSum = 0;
for (let i = 0; i < dicesum.length; i++) {
  totalSum += dicesum[i];
}
console.log("Kaikkien heittojen summa", totalSum)

const output = document.getElementById('diceroll');
function updateInfo(info) {
  output.textContent = info;
  }
  updateInfo(`Nopan heittojen summa:  ${totalSum}`);


//tehtävä 8
  const startYear = parseInt(prompt('Anna aloitus vuosi'));
  const endYear = parseInt(prompt('Anna lopetusvuosi'));
  const yearresults = []

  function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
  }

  for (let year = startYear; year <= endYear; year++) {
    if (isLeapYear(year)) {
      yearresults.push(year);
    }
  }
console.log(yearresults)

let vuosilista = document.getElementById("vuosilista");
  for (let i = 0; i < yearresults.length; ++i) {
    let li = document.createElement('li');
    li.innerText = yearresults[i];
    vuosilista.appendChild(li);
  }


// tehtävä 9
const primetest = parseInt(prompt('test if the number is prime number'))
function isPrime(num) {
    if (num <= 1) return false;
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}
document.querySelector('#primenumber').innerHTML = `Is ${primetest} a prime number? : ${isPrime(primetest)}`
