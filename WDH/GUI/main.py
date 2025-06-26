

import tkinter as tk
from tkinter import ttk

einnahmen = []
ausgaben = []

def update_uebersicht():
    gesamt_einnahmen = sum(einnahmen)
    gesamt_ausgaben = sum(ausgaben)
    saldo = gesamt_einnahmen - gesamt_ausgaben
    text = (
        f"Gesamteinnahmen: {gesamt_einnahmen:.2f} €\n"
        f"Gesamtausgaben: {gesamt_ausgaben:.2f} €\n"
        f"Saldo: {saldo:.2f} €"
    )
    label_uebersicht.config(text=text)

def einnahme_hinzufuegen():
    try:
        betrag = float(entry_betrag.get())
        beschreibung = entry_beschreibung.get()
        einnahmen.append(betrag)
        listbox.insert(tk.END, f"+ {betrag:.2f} €: {beschreibung}")
        update_uebersicht()
        entry_betrag.delete(0, tk.END)
        entry_beschreibung.delete(0, tk.END)
    except ValueError:
        label_uebersicht.config(text="Bitte einen gültigen Betrag eingeben.")

def ausgabe_hinzufuegen():
    try:
        betrag = float(entry_betrag.get())
        beschreibung = entry_beschreibung.get()
        ausgaben.append(betrag)
        listbox.insert(tk.END, f"- {betrag:.2f} €: {beschreibung}")
        update_uebersicht()
        entry_betrag.delete(0, tk.END)
        entry_beschreibung.delete(0, tk.END)
    except ValueError:
        label_uebersicht.config(text="Bitte einen gültigen Betrag eingeben.")

root = tk.Tk()
root.title("Konto")
root.geometry("400x400")

frame_eingabe = ttk.Frame(root)
frame_eingabe.pack(pady=10)

ttk.Label(frame_eingabe, text="Betrag:").grid(row=0, column=0, padx=5, pady=5)
entry_betrag = ttk.Entry(frame_eingabe)
entry_betrag.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_eingabe, text="Beschreibung:").grid(row=1, column=0, padx=5, pady=5)
entry_beschreibung = ttk.Entry(frame_eingabe)
entry_beschreibung.grid(row=1, column=1, padx=5, pady=5)

frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=5)

btn_einnahme = ttk.Button(frame_buttons, text="Einnahme hinzufügen", command=einnahme_hinzufuegen)
btn_einnahme.grid(row=0, column=0, padx=5)

btn_ausgabe = ttk.Button(frame_buttons, text="Ausgabe hinzufügen", command=ausgabe_hinzufuegen)
btn_ausgabe.grid(row=0, column=1, padx=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

label_uebersicht = ttk.Label(root, text="Gesamteinnahmen: 0.00 €\nGesamtausgaben: 0.00 €\nSaldo: 0.00 €")
label_uebersicht.pack(pady=10)

root.mainloop()