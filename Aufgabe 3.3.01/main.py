
from bankkonto import BankAccount

print("Test: Einzahlen + Zinsen:")
acc1 = BankAccount("Max Mustermann")
acc1.einzahlen(100)
acc1.zinsen_berechnen(2)
print(acc1)

print("\nTest: Konto überziehen:")
acc1.abheben(203)
