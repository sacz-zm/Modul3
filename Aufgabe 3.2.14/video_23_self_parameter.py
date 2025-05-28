

class Car: 
    def __init__(self): 
        self.car_brand = None 
        self.horse_power = None
        self.color = None
# self gibt automatisch die Referenz auf das aktuelle Objekt mit, wenn die __init__ Methode aufgerufen wird
# Python kann dadurch eindeutig zuordnen, welches Attribut von welchem konkreten Objekt geändert werden soll
car_1 = Car() 

print(car_1.car_brand) 

car_1.car_brand = "Audi"
car_1.horse_power = 250
car_1.color = "Blau"

print(car_1.car_brand)
print(car_1.horse_power)
print(car_1.color)

car_2 = Car() 
car_2.car_brand = "BMW"
car_2.horse_power = 210
car_2.color = "Schwarz"

car_3 = car_1
# car_3 und car_1 greifen auf das selbe Objekt zu | Referenz ist die selbe 

print(car_1)
print(car_2)
print(car_3)
# Zahl nach at ist eine Referenz
# Sobald ein Objekt erstellt wird, wird Speicher für dieses Objekt reserviert
# Auf diesem Speicher werden die einzelnden Atrribute und somit Daten des Objektes gespeichert
# Referenz in Variable zeigt auf die Start-Adresse des Speicherbreichs, in welchem alle Daten des Objektes gespeichert sind
