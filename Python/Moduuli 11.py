class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi: {self.nimi}, Lehden päätöimittaja: {self.päätoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}, Kirjan kirjoittaja: {self.kirjoittaja}, Sivumäärä:  {self.sivumäärä}")


julkaisut = []
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka","Aki Hyyppä"))
julkaisut[0].tulosta_tiedot()
julkaisut[1].tulosta_tiedot()