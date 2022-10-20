class Drucker:
    marke: str 
    farbe: str
    max_papier_drucken: int
    min_papier_drucken: int
    aktuell_papier_drucken: int

    def __init__(self, farbe, marke) -> None:
        self.marke = marke 
        self.farbe = farbe 

    def max_papier_drucken(self):
        self.aktuell_papier_drucken = self.max_papier_drucken

    def min_papier_drucken(self):
        self.min_papier_drucken = 1


Drucker_von_Stefan = Drucker(Farbe = "weiß", Marke = "HP")


Drucker_von_Stefan.max_papier_drucken()
Drucker_von_Stefan.min_papier_drucken()