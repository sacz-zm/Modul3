

class BankAccount:
    
    def __init__(self, name, limit=-100):
        self.kontoinhaber = name
        self.kontostand = 0.0
        self.limit = limit
        
         
    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
         
    def abheben(self, betrag):
        if self.kontostand - betrag >= self.limit:
            self.kontostand -= betrag
        else: 
            print("Überziehungsrahmen erreicht")
  
    def zeige_kontostand(self):
        print(self.kontostand)

    def __str__(self):
        return f"Konto von {self.kontoinhaber} - Kontostand: {self.kontostand:.2f}€"
    
    def zinsen_berechnen(self, zinssatz):
        if self.kontostand > 0:
            zinsen = (self.kontostand / 100) * zinssatz
            self.kontostand += zinsen

        
print("Test: Einzahlen + Zinsen:")
acc1 = BankAccount("Max Mustermann")
acc1.einzahlen(100)
acc1.zinsen_berechnen(2)
print(acc1)

print("\nTest: Konto überziehen:")
acc1.abheben(203)





