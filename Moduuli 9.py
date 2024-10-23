import random
from prettytable import PrettyTable
table=PrettyTable()

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, aika):
        self.matkamittari += self.nopeus * aika
#tehtävä1
Saab = Auto(rekisteritunnus="Saa-81", huippunopeus=140)
print(f"Rekisteritunnus: {Saab.rekisteritunnus} Huippunopeus: {Saab.huippunopeus}")

Saab.kiihdytä(30)
Saab.kiihdytä(70)
Saab.kiihdytä(50)
print(f"Auton nopeus: {Saab.nopeus} KM/H")
Saab.kiihdytä(-200)
print(f"Auton nopeus: {Saab.nopeus} KM/H")

Saab1 = Auto(rekisteritunnus="Saa-812", huippunopeus=140,)
Saab1.matkamittari = 2000
Saab1.nopeus = 60
print(f"Saabilla on ajettu: {Saab1.matkamittari} kilometriä")
Saab1.kulje(1.5)
print(f"Saabilla on ajettu {Saab1.matkamittari} kilometriä")

autot = []
for i in range(10):
    rekisteritunnus = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(auto)

#for auto in autot:
    #print(f"Rekisteritunnus: {auto.rekisteritunnus}, Huiput: {auto.huippunopeus}")

kilpailupäällä = True
tunnit = 0

while kilpailupäällä:
    tunnit += 1

    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

    if any(auto.matkamittari >= 10000 for auto in autot):
        kilpailupäällä = False


print(f"Kilpailu päättyi {tunnit} tunnin jälkeen.")

print("Tulokset:")
for auto in sorted(autot, key=lambda  x: x.matkamittari, reverse=True):
    print(f"Rekisteritunnus: {auto.rekisteritunnus},  Matka: {auto.matkamittari} Kilometriä, "
          f"Huippunopeus: {auto.huippunopeus} KM/H, Keskinopeus: {auto.matkamittari/tunnit:.2f} KM/H")

table.field_names = ["Rekisteritunnus", "Matka(KM)", "Huippunopeus(KM/H)", "Keskinopeus(KM/H)"]
for auto in autot:
    table.add_row([auto.rekisteritunnus, auto.matkamittari, auto.huippunopeus, int(auto.matkamittari/tunnit)])

print("Kilpailun tulokset ovat:")
print(table.get_string(sortby="Matka(KM)", reversesort=True))