

# Ohne Anpassung
sum = 0
for element in range(1, 101):
    if element % 2 == 0:
        sum += element
print(f"Die Summer aller gerade Zahlen ist: {sum}")

# Anpassung

insert = int(input("Bis zur welcher Zahl soll summiert werden? "))

sum = 0
for element in range(1, insert + 1 ): # + 1 weil sonst der eingebene Endwert exkludiert wird
    if element % 2 == 0:
        sum += element
print(f"Die Summe aller geraden Zahlen bis {insert} ist {sum}")
