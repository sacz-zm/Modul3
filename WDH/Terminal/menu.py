

from ein import einnahmen_hinzufuegen
from aus import ausgaben_hinzufuegen
from sicht import sicht

def menu():
    gein = []
    gaus = []
    while True:
        print("Was möchten Sie tun?")
        print("""    1 - Einnahmen hinzufügen
    2 - Ausgaben hinzufügen
    3 - Übersicht anzeigen
    4 - Beenden""")
        option = input("Bitte wählen Sie eine Option (1-4): ")

        if option == "1":
            einnahmen_hinzufuegen(gein)
        elif option == "2":
            ausgaben_hinzufuegen(gein, gaus)
        elif option == "3":
            sicht(gein, gaus)
        elif option == "4":
            print("Programm wird beendet.")
            break
        else:
            print("Ungültige Option. Bitte wählen Sie 1, 2, 3 oder 4.")