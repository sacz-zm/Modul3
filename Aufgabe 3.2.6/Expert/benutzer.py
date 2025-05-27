

print("Errate die Zahl!\n")

import random
number = random.randint(1, 100)
tries = 0
goal = False

while not goal:
   
    guess = int(input("Gebe eine Ganzzahl zwischen 1 - 100 ein: "))
    tries += 1


    if guess < number:
            print(f"Die gesuchte Zahl ist höher als {guess}")
    
    elif guess > number:
            print(f"Die gesuchte Zahl niederiger als {guess}")

    else:
        print(f"""{guess} ist korrekt!
Du hast {tries} Versuche gebraucht""")
        goal = True
