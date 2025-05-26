

print("10% Rabatt!")

wert = int(input("Einkaufswert: "))
if wert >= 100:
    print(f"Endpreis: {wert - (wert / 100 * 10)}€")
else:
    print(f"Bei einem Wert von {wert}€ erhalten Sie keinen Rabatt!")