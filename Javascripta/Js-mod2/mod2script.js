'use strict';
// tehtävä 1
const luvut = [];
for (let i = 1; i < 6; i++) {
  let luku = parseFloat(prompt('Anna luku'));
  luvut.push(luku);
}
for (let i = 5; i >= 0; i--) {
  console.log(luvut[i])
}
// tehtävä 2
const osallistujat = parseFloat(prompt('Kuinka monta osallistujaa?'));
const osallistujalista = [];
for (let i = 0; i < osallistujat; i++) {
  let osallistuja = prompt('Anna osallistujan nimi');
  osallistujalista.push(osallistuja)
}
let listausosallistujat = document.getElementById("osallistujalista");
  for (let i = 0; i < osallistujat; i++) {
    let li = document.createElement('li');
    li.innerText = osallistujalista[i];
    listausosallistujat.appendChild(li);
  }
//tehtävä 3
const dogamount = 6
const doglist = []
for (let i = 0; i < dogamount; i++) {
  let dogname = prompt('Anna koiran nimi')
  doglist.push(dogname)
  doglist.sort().reverse()
}
let koiralistaus = document.getElementById('koiralista')
  for (let i = 0; i < dogamount; i++) {
  let li = document.createElement('li')
  li.innerText = doglist[i];
  koiralistaus.appendChild(li)
  }
//tehtävä 6ja7

function noppa(sides) {
    let diceresult = Math.floor(Math.random() * sides) + 1;
    return diceresult;
}

function dicethrow() {
    let nopanheitto = 0;
    const sides = parseFloat(prompt('Anna nopan sivujen määrä'))
    while (nopanheitto !== sides) {
      nopanheitto = noppa(sides);
      console.log(nopanheitto)
      document.getElementById('noppa').innerHTML += "<li>" + nopanheitto +  "</li>";
    }
}
dicethrow();

//tehtävä 10

function createCandidate(name) {
    return {
        name: name,
        voteamount: 0,
        addVote: function() {
            this.voteamount += 1;
        }
    };
}

const candidates = []

const amountOfCandidates = parseFloat(prompt('Anna ehdokkaiden lukumäärä'))
for (let i = 1; i <= amountOfCandidates; i++) {
 let ehdokas = prompt('Ehdokkaan ' + [i] + ' nimi?')
 candidates.push(createCandidate(ehdokas))

}
const howManyVotes = parseFloat(prompt('Montako ääntä?'))
let emptyvote = 0;
for (let i = 0; i < howManyVotes; i++) {
  let votewho = (prompt(`Kenelle annat äänen? (1 - ${amountOfCandidates})`))
   if (votewho === null || votewho.trim() === '' || isNaN(votewho)) {
    emptyvote += 1;
    continue; }
     let koodikierto = parseInt(votewho)
  koodikierto = votewho - 1;
  if (koodikierto < 0 || koodikierto >= candidates.length) {
    emptyvote += 1;
  } else {
    candidates[koodikierto].addVote();
  }
}
candidates.sort((a, b) => a.voteamount  - b.voteamount ).reverse()

console.log(`The winner is ${candidates[0].name} with ${candidates[0].voteamount} votes`)
candidates.forEach(candidate => {
    console.log(`${candidate.name}: ${candidate.voteamount} ääntä`);
});
console.log(`Tyhjiä ääniä: ${emptyvote}`)