

class Car: # class + Bezeichner erstellt eine Klasse | Bezeichner der Klasse mit Großbuchstaben anfangen
    def __init__(self): # def + __init__() definiert eine Funktion | In dieser werden die Attribute definiert
        self.car_brand = None # Alles nach self. kann beliebig gewählt werden | Attribut braucht einen Wert | None als Platzhalter
        self.horse_power = None
        self.color = None
        
# Klasse ist erstmal nur ein Bauplan

car_1 = Car() 
# Car() erstellt ein Objekt von der Klasse Car | Rückgabewert ist die Referenz auf das Objekt | car_1 = speichert die Referenz des Objektes Car() in der Variable
# Über die Variable car_1 kann auf das Objekt zugriffen werden

# Bei Ausführung: 
# 1. Die Klassendefinition wird gelesen | Python ist bewusst, dass es eine selbst definierte Klasse namens Car gibt
# 2. Die Klasse wird genutzt um das Objekt zu erstellen
# Methode = Eine Funktion innerhalb einer Klasse

print(car_1.car_brand) 
# print(variable.attribut) Gibt den Wert des Attributes aus

car_1.car_brand = "Audi"
car_1.horse_power = 250
car_1.color = "Blau"
# [variable.attribut =] weist dem Attribut einen neuen Wert zu
print(car_1.car_brand)
print(car_1.horse_power)
print(car_1.color)

car_2 = Car() # Erstellt ein zweites Objekt 
car_2.car_brand = "BMW"
car_2.horse_power = 210
car_2.color = "Schwarz"
# [variable.attribut =] weist dem Attribut einen neuen Wert zu
print(car_2.car_brand)
print(car_2.horse_power)
print(car_2.color)

# Die Klasse ist der übergreifende Bauplan
# Dadurch kann man ganz individuell einen eigenen Datentypen definieren
# Definition der Klasse alleine bringt noch nichts
# Druch klassennamen() muss ein konkretes Objekt erstellt werden
# Jedes erstellte Objekt ist einzelnd zu betrachten
# Von der Klasse können beliebig viele Objekte erstellt werden
# Die Objekte haben zwar die gleiche Attribute (Da in der Klasse vorgegeben)
# Die Werte können aber für jedes Objekt einzelnd modifizieren
