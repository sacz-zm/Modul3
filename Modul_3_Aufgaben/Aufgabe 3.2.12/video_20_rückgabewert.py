

def say_hello(first_name, last_name): 
    
    print(print("Hallo " + first_name + " " + last_name))
    print("Willkommen zurück")

print(type(say_hello("Sascha", "Czoske"))) 

# return

def maximum(a, b):
    if a < b:
        return b
    else: 
        return a
result = maximum(3, 7)
print(result)

#####################################################

# Jede Funktion gibt einen Wert zurück
# None ein Platzhalter Wert
# Basisdatentyp: NoneType
# "return" Funktion wird beendet und der Wert nach return wird zurückgegeben
