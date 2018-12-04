class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return self.imie + " " + self.nazwisko

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def wyplata(self):
        return self.pensja * 1.2

class Kierownik(Pracownik):
    """
    def __init__(self, imie, nazwisko, pensja):
        Pracownik.__init__(self, imie, nazwisko, pensja)
    """

    def wyplata(self):
        return super().wyplata() + 1200.0

o = Osoba("Jan",  "Kowalski")
print(o)

p = Pracownik("Jan", "Nowak", 2250)

print("{0} wypłata {1}".format(p, p.wyplata()))

k = Kierownik("Anna", "", 5000)
print(k.wyplata())