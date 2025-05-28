

# Celsius zu Fahrenheit

def cel_to_f(cel):
    return cel * 9 / 5 + 32

# Fahrenheit zu Celsius

def f_to_cel(f):
    return (f - 32) * 5 / 9

# Schleife

end = False
while not end:

# Abfrage Umrechnung

    print("\nWelche Umrechung soll stattfinden?\n")
    print("Für Celsius zu Fahrenheit die '1' eingeben")
    print("Für Fahrenheit zu Celsius die '2' eingeben")
    print("Beenden Sie das Programm mit 'stop'\n")
    insert = input("Auswahl: ")
    
# Abfrage Temperatur

    if insert == "1":
        temp = float(input("Gebe die Temperatur in Celsius ein: "))
        result = cel_to_f(temp)
        print(f"\n{temp} °C sind {result} °F")
    elif insert == "2":
        temp = float(input("Gebe die Temperatur in Fahrenheit ein: "))
        result = f_to_cel(temp)
        print(f"\n{temp} °F sind {result} °C \n")
    elif insert == "stop":
        end = True
    else: 
        print("Eingabe ungültig!")
    

