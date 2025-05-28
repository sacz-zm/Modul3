

numbers_1 = [4, 7, 2, 9, 1, 5, 3]

# Einfach

print(f"Die Liste enthält {len(numbers_1)} Elemente") # len um die Länge anzuzeigen
print(f"Die Größte Zahl in der Liste ist: {max(numbers_1)}") # max gibt die größte Zahl aus
print(f"Die kleinste Zahl in der Liste ist: {min(numbers_1)}") # min gibt die kleinste Zahl aus

# Mittel

avg = sum(numbers_1) / len(numbers_1) # Durchschnitt = Summe / Länge
print(f"Der Durchschnittssumme der Elemente liegt bei: {avg}")
print(f"Die umgekehrte Reihenfolge der Liste lautet: {numbers_1[::-1]}") # [::-1] zeigt die komplette Liste in umgekehrter Reihenfolge

# Experte

even = [x for x in numbers_1 if x % 2 == 0] 
# Erstellt eine neue Liste aus allen Elementen, bei die denen das Element gerade ist
# x ist nur ein Platzhalter für die einzelnen Elemente während damit gearbeitet wird
print(f"Die geraden Zahlen sind: {even}")



