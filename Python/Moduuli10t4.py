import random

class Auto:

    tehty = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, matkamittari=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matkamittari = matkamittari
        Auto.tehty = Auto.tehty + 1

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

class Kilpailu:
    def __init__(self, nimi: str, pituus: float, osallistujat: list):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    def tunti_kuluu(self):
        for auto in self.osallistujat:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytä(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_järjestys(self):
        print(f"Kilpailun: {self.nimi} tilanne: {tunnit} tunnin jälkeen.")
        järjestetyt_autot = sorted(self.osallistujat, key=lambda auto: auto.matkamittari, reverse=True)
        for sijoitus, auto in enumerate(järjestetyt_autot, start=1):
            print(f"{sijoitus}: Auto: {auto.rekisteritunnus}, Nopeus: {auto.nopeus} KM/H, Ajettu: {auto.matkamittari}KM")

    def kilpailu_ohi(self):
        return any(auto.matkamittari >= self.pituus for auto in self.osallistujat)


autot = []
for i in range(10):
    rekisteritunnus = f"ABC-{i + 1}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))


kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunnit = 0
while not kilpailu.kilpailu_ohi():
    tunnit += 1
    kilpailu.tunti_kuluu()
    if tunnit % 10 == 0:
        kilpailu.tulosta_järjestys()

print("Kilpailu on päättynyt!!")
kilpailu.tulosta_järjestys()
print(f"Kilpailu kesti {tunnit} tuntia!")