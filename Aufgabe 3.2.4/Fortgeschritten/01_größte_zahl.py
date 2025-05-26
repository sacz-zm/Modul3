

print("Welches ist die größte Zahl?")

print("Gebe drei Zahlen ein: ")
number_1 = int(input("Erste Zahl: "))
number_2 = int(input("Zweite Zahl: "))
number_3 = int(input("Dritte Zahl: "))

if number_1 > number_2 and number_1 > number_3:
    print(number_1)
elif number_2 > number_1 and number_2 > number_3:
    print(number_2)
else:
    print(number_3)
    