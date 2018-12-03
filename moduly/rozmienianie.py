def rozmien(portmonetka, kwota):
    wynik = [0] * len(portmonetka)
    zostalo = kwota
    for nominal in reversed(range(len(portmonetka))):
        if zostalo <= 0:
            break
        if portmonetka[nominal] == 0:
            continue
        liczba_nominalow = min(zostalo // nominal, portmonetka[nominal])
        print(zostalo, nominal, liczba_nominalow)
        zostalo -= nominal * liczba_nominalow
        portmonetka[nominal] = portmonetka[nominal] - liczba_nominalow
        wynik[nominal] = liczba_nominalow
    while zostalo > 0:
        for nominal in reversed(range(len(portmonetka))):
            if portmonetka[nominal] > 0:
                zostalo = zostalo - nominal
                portmonetka[nominal] -= 1
                wynik[nominal] += 1
        # całkiem pusta portmonetka
        if portmonetka == ([0] * len(portmonetka)):
            break
    # print(suma)
    return wynik, zostalo
