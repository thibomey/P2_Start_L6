class Spelbibliotheek:
    def __init__(self):
        self.spellen = []

    def voeg_spel_toe(self, spel):
        self.spellen.append(spel)

    def verwijder_spel(self, spel):
        if spel in self.spellen:
            self.spellen.remove(spel)

    def toon_spellen(self):
        print("\nDIY STEAM:")
        for spel in self.spellen:
            print(spel.titel)

    def toon_details(self, spel_titel):
        gevonden_spel = None
        for spel in self.spellen:
            if spel.titel == spel_titel:
                gevonden_spel = spel
                break

        if gevonden_spel:
            print("\nSpel Details:")
            print("Titel:", gevonden_spel.titel)
            print("Genre:", gevonden_spel.genre)
            print("Platform:", gevonden_spel.platform)
            print("Prijs:", gevonden_spel.prijs)
        else:
            print("\nSpel niet gevonden in de bibliotheek.")