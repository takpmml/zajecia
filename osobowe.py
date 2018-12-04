class Osoba:

    def __init__(self, imie, nazwisko, wzrost = 178, waga=70):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return self.__class__.__name__ + ": " + self.imie + " " + self.nazwisko

class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja, wzrost, waga):
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


o = Osoba("Jan",  "Kowalski", 1.78, 60)
o.wzrost = 182
print(o)

p = Pracownik("Jan", "Nowak", 2250, 1.65, 70)

print("{0} wypłata {1}".format(p, p.wyplata()))

k = Kierownik("Anna", "", 5000)
print(k.wyplata())