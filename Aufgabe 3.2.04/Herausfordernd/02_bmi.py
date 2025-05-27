

print("BMI-Rechner")

weight = float(input("Ihr Gewicht in Kg: "))
height = float(input("Ihre Größe in Metern: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Sie haben Untergewicht")
elif bmi > 18.5 and bmi < 30:
    print("Sie haben Normalgewicht")
else:
    print("Sie haben Übergewicht")
