class Drucker:
    Marke: str 
    anzahl_patronen: int
    Farbe: str
    max_papier_drucken: int
    min_papier_drucken: int
    aktuell_papier_drucken: int
    power: True

    def __init__(self, Farbe, Marke) -> None:
        self.marke = Marke 
        self.farbe = Farbe 

    def max_papier_drucken(self):
        self.aktuell_papier_drucken = self.max_papier_drucken

    def min_papier_drucken(self):
        self.min_papier_drucken = 1

    def d_an(self):
        self.power = True
    def d_aus(self):
        self.power = False 


Drucker_von_Stefan = Drucker(Farbe = "weiß", Marke = "HP")
Drucker_von_Stefan.anzahl_patronen = 4


Drucker_von_Stefan.max_papier_drucken()
Drucker_von_Stefan.min_papier_drucken()