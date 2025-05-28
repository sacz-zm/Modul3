

print("Dazwischen oder nicht?")

print("Gebe drei Zahlen ein: ")
number_1 = int(input("Erste Zahl: "))
number_2 = int(input("Zweite Zahl: "))
number_3 = int(input("Dritte Zahl: "))

if number_1 > number_2 > number_3 or number_1 < number_2 < number_3:
    print(f"{number_2} liegt zwischen {number_1} und {number_3}")
else:
    print(f"{number_2} liegt nicht zwischen {number_1} und {number_3}")