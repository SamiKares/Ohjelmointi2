class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.kerrosnyt = alinkerros

    def kerrosylös(self):
        if self.kerrosnyt == self.ylinkerros:
            print("Olet jo huipulla")
        else:
            self.kerrosnyt += 1
        return

    def kerrosalas(self):
        if self.kerrosnyt == self.alinkerros:
            print("Olet jo pohjalla")
        else:
            self.kerrosnyt -= 1
        return

    def siirrykerrokseen(self, mihinkerrokseen):
        kerrostensiirtymä = abs(self.kerrosnyt - mihinkerrokseen)
        if mihinkerrokseen == self.kerrosnyt:
            mihinkerrokseen = self.kerrosnyt
        if mihinkerrokseen > self.kerrosnyt:
            for i in range(kerrostensiirtymä):
                self.kerrosylös()
            #print(f"Olet nyt kerroksessa {self.kerrosnyt}")
        if mihinkerrokseen < self.kerrosnyt:
            for i in range(kerrostensiirtymä):
                self.kerrosalas()
            #print(f"Olet nyt kerroksessa {self.kerrosnyt}")

class Talo:
    def __init__(self, alinkerros, ylinkerros, hissien_lkm):
        self.hissit = []
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alinkerros, ylinkerros))

    def aja_hissiä(self, hissin_numero, mihinkerrokseen):
        if 0 <= hissin_numero <= len(self.hissit):
            print(f"Ajetaan hissillä: {hissin_numero} kerrokseen: {mihinkerrokseen} ")
            self.hissit[hissin_numero].siirrykerrokseen(mihinkerrokseen)
        else:
            print("Väärä hissinumero!")

    def kerrokset(self):
        print("Hissien sijainnit:")
        for i, hissi in enumerate(self.hissit):
            print(f"Hissi {i} on kerroksessa {hissi.kerrosnyt}")

    def palohälytys(self):
        print("!!!!PALOHÄLYTYS!!!!")
        for hissi in self.hissit:
            hissi.siirrykerrokseen(hissi.alinkerros)

h = Hissi(1,10)
h.siirrykerrokseen(5)
h.siirrykerrokseen(1)
print(h.kerrosnyt)

talo = Talo(-2,10, 4)
talo.aja_hissiä(0,5)
talo.aja_hissiä(1,3)
talo.aja_hissiä(2,7)
talo.aja_hissiä(3, 9)
talo.kerrokset()
talo.palohälytys()
talo.kerrokset()