
# Klasa to szablon
class Czlowiek(object):
    gatunek = "Homo sapiens"
    def __init__(self, imie):
        self._imie = imie
    def przedstawSie(self):
        print("Mam na imie ", self._imie)

class Dziecko(Czlowiek):
    def baw_sie(self):
        print("Ale zabawa, Juhuuu")
    
    def przedstawSie(self):
        print("Cesc jestem ", self._imie)

# Obiekt (instancja klasy)
adam = Czlowiek("Adam")
adam.przedstawSie()
adam._imie = 'Test'
adam.przedstawSie()

kain = Dziecko("Kain")
kain.przedstawSie()
kain.baw_sie()

