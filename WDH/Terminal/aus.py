

def ausgaben_hinzufuegen(gein, gaus):
            betrag = float(input("Bitte geben Sie den Betrag ein: "))
            gaus.append(betrag)
            print(f"      Ausgaben in Höhe von {betrag} € wurden abgezogen")
            saldo = sum(gein) - sum(gaus)
            if saldo < 0:
                print("Achtung: Budget überschritten!")