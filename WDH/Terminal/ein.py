

def einnahmen_hinzufuegen(gein):
    betrag = float(input("Bitte geben Sie den Betrag ein: "))
    gein.append(betrag)
    print(f"      Einnahmen in Höhe von {betrag} € wurden hinzugefügt")