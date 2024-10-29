import random


class Auto:
    def __init__(self, merkki: str, rekisterinumero: str, huippunopeus: float):
        self.merkki = merkki
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matkamittari = 0

    def kulje(self, aika):
        self.matkamittari += self.nopeus * aika

    def tulosta_tiedot(self):
        print(f"Merkki: {self.merkki}, Rekisterinumero: {self.rekisterinumero}, Huippunopeus(KM/H): {self.huippunopeus},")

    def kisailu(self):
        print(f"{self.merkki} ajoi yhteensä: {self.matkamittari} kilometriä")


class Sähköauto(Auto):
    def __init__(self, merkki, rekisterinumero, huippunopeus, akunkapasiteetti: float):
        super().__init__(merkki, rekisterinumero, huippunopeus)
        self.akunkapasiteetti = akunkapasiteetti

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Akun kapasiteetti: {self.akunkapasiteetti} KWH")

    def kulutus(self):
        kuluttaa = self.matkamittari * 0,1
        rangea = self.akunkapasiteetti - kuluttaa
        print(rangea)

class Polttomoottori(Auto):
    def __init__(self, merkki, rekisterinumero, huippunopeus, bensatankki: float):
        super().__init__(merkki, rekisterinumero, huippunopeus)
        self.bensatankki = bensatankki

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Bensatankin koko: {self.bensatankki} litraa")

autot = []
autot.append(Sähköauto("Tesla", "TES-70", 267,52.5,))
autot.append(Polttomoottori("Mersu", "MER-55", 285, 120 ))

autot[0].nopeus = 155
autot[1].nopeus = 167
for t in autot:
    t.kulje(3)
for t in autot:
    t.kisailu()

