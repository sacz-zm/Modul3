

print("Schaltjahr oder nicht?")

year = int(input("Gebe ein Jahr ein: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} ist ein Schaltjahr")
else: 
    print(f"{year} ist kein Schaltjahr")
