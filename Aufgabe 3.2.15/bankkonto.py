

class BankAccount: 
    # Konstruktor: Initialisiert ein neues Bankkonto mit Name des Kontoinhabers und einem optionalen Überziehungslimit
    def __init__(self, name, limit=-100):
        self.kontoinhaber = name        # Name des Kontoinhabers
        self.kontostand = 0.0           # Startkontostand ist 0 €
        self.limit = limit              # Überziehungslimit (z. B. -100 €)

    # Methode zum Einzahlen eines Betrags auf das Konto
    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag   # Betrag wird zum Kontostand hinzugefügt

    # Methode zum Abheben eines Betrags, sofern das Limit nicht überschritten wird
    def abheben(self, betrag):
        if self.kontostand - betrag >= self.limit:
            self.kontostand -= betrag   # Betrag wird abgezogen
        else: 
            print("Überziehungsrahmen erreicht")  # Warnung bei Limitüberschreitung

    # Methode zur Anzeige des aktuellen Kontostands
    def zeige_kontostand(self):
        print(self.kontostand)

    # String-Darstellung des Kontos, z. B. für `print(konto)`
    def __str__(self):
        return f"Konto von {self.kontoinhaber} - Kontostand: {self.kontostand:.2f}€"
    
    # Methode zur Berechnung und Gutschrift von Zinsen (nur bei positivem Kontostand)
    def zinsen_berechnen(self, zinssatz):
        if self.kontostand > 0:
            zinsen = (self.kontostand / 100) * zinssatz
            self.kontostand += zinsen   # Zinsen werden gutgeschrieben


        
print("Test: Einzahlen + Zinsen:")
acc1 = BankAccount("Max Mustermann")
acc1.einzahlen(100)
acc1.zinsen_berechnen(2)
print(acc1)

print("\nTest: Konto überziehen:")
acc1.abheben(203)





