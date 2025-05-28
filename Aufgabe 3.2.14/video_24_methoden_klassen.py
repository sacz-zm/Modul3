

class Car: 
    def __init__(self): 
        self.car_brand = None 
        self.horse_power = None
        self.color = None
        self.x_position = 5 # Car Objekt liegt auf der x Koordinate 5 
        self.y_position = 5 # Car Objekt liegt auf der y Koordinate 5

    
    def drive(self,x ,y): # Methode zum Fahren
        self.x_position += x # x Koordinate verändert sich um den Wert x
        self.y_position += y # y Koordinate verändert sich um den Wert y


car_1 = Car() 
print(car_1.x_position) # Gibt anfangs x Koordinate des Objektes car_1 aus 
print(car_1.y_position) # Gibt anfangs y Koordinate des Objektes car_1 aus
car_1.drive(5, 10) # Veränderung der Koordinaten self.x_position += x und self.x_position += y | x Koordinate wird um 5 erhöht | y Koordinate wird um 10 erhöht
print(car_1.x_position) # Gibt neue x Koordinate des Objektes aus
print(car_1.y_position) # Gibt neue y Koordinate des Objektes aus
