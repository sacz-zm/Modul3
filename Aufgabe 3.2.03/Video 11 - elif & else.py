

age = int(input("Bitte gebe dein Alter ein: "))

if age < 21: 
    print("Achtung, der Nutzer ist jünger als 18") 
elif age == 18:
    print("Der Nutzer ist exakt 18")
elif age == 19:
    print("Der Nutzer ist exakt 19")
else:
    print("Der Nutzer ist volljährig")

print("Programmende")

###################################################################
# else muss auf der gleichen Einrückungsebene wie das if liegen 
# auf das es sich bezieht

