

end = False
end_2 = "stop"
inserts = [] # Erstellt ein leere Liste

while not end:
    insert = input('Gebe ein Zahl oder "stop" ein: ')
    if insert == end_2:
        end = True
    if insert.isdigit(): # .isdigit() filtert nicht Zahlen
        inserts.append(insert) # .append speichert Eingaben in der Liste
print(inserts)

numbers = [int(element) for element in inserts] # Da die inserts als String gespeichert werden
numbers.sort()                      # .sort() sortiert die Zahlen aufsteigend
min_number = numbers[0]
max_number = numbers[0]
total = 0
for element in numbers:
    if element < min_number:
        min_number = element
    if element > max_number:
        max_number = element
    total += element
avg = total / len(numbers)
print(f"Die kleinste Zahl ist: {min_number}")
print(f"Die größte Zahl ist: {max_number}")
print(f"Der Durchschnitt der Summe liegt bei: {avg}")
print(f"Sortierung: {numbers}")
