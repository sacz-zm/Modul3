import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Datenhaltung
einnahmen = []
ausgaben = []

# Fenstergrößen
START_BREITE = 400
START_HOEHE = 450

# --- Hilfsfunktionen ---
def get_kategorie():
    return kategorie_var.get()

def finde_kategorie_index(kategorie):
    """Sucht oder erstellt eine Kategorie-Überschrift in der Listbox."""
    for i in range(listbox.size()):
        if listbox.get(i) == f"--- {kategorie} ---":
            return i
    listbox.insert(tk.END, f"--- {kategorie} ---")
    idx = listbox.size() - 1
    listbox.itemconfig(idx, {'fg': 'blue'})
    return idx

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

# --- Hauptfunktionen ---
def einnahme_hinzufuegen():
    try:
        betrag = float(entry_betrag.get())
        beschreibung = entry_beschreibung.get()
        kategorie = get_kategorie()
        einnahmen.append(betrag)
        datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        eintrag = f"{datum} | + {betrag:.2f} €: {beschreibung}"
        idx = finde_kategorie_index(kategorie)
        # Finde die nächste Kategorie oder das Ende
        insert_idx = idx + 1
        while insert_idx < listbox.size() and not listbox.get(insert_idx).startswith("---"):
            insert_idx += 1
        listbox.insert(insert_idx, eintrag)
        listbox.itemconfig(insert_idx, {'fg': 'green'})
        update_uebersicht()
        entry_betrag.delete(0, tk.END)
        entry_beschreibung.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Ungültiger Wert", "Bitte einen gültigen Betrag eingeben")

def ausgabe_hinzufuegen():
    try:
        betrag = float(entry_betrag.get())
        beschreibung = entry_beschreibung.get()
        kategorie = get_kategorie()
        ausgaben.append(betrag)
        datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        eintrag = f"{datum} | - {betrag:.2f} €: {beschreibung}"
        idx = finde_kategorie_index(kategorie)
        insert_idx = idx + 1
        while insert_idx < listbox.size() and not listbox.get(insert_idx).startswith("---"):
            insert_idx += 1
        listbox.insert(insert_idx, eintrag)
        listbox.itemconfig(insert_idx, {'fg': 'red'})
        update_uebersicht()
        entry_betrag.delete(0, tk.END)
        entry_beschreibung.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Ungültiger Wert", "Bitte einen gültigen Betrag eingeben")

def clear_liste():
    listbox.delete(0, tk.END)

def speichern():
    with open("buchungen.txt", "w", encoding="utf-8") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i) + "\n")

def datei_oeffnen():
    START_BREITE2 = 500
    START_HOEHE2 = 425
    fenster = tk.Toplevel(root)
    fenster.title("Buchungen (buchungen.txt)")
    fenster.geometry(f"{START_BREITE2}x{START_HOEHE2}")

    def min_groesse2(event):
        breite = fenster.winfo_width()
        hoehe = fenster.winfo_height()
        if breite < START_BREITE2 or hoehe < START_HOEHE2:
            fenster.geometry(f"{max(breite, START_BREITE2)}x{max(hoehe, START_HOEHE2)}")
    fenster.bind("<Configure>", min_groesse2)

    textfeld = tk.Text(fenster, wrap="word")
    textfeld.pack(expand=True, fill="both")
    textfeld.tag_configure("einnahme", foreground="green")
    textfeld.tag_configure("ausgabe", foreground="red")
    try:
        with open("buchungen.txt", "r", encoding="utf-8") as f:
            for zeile in f:
                if "| +" in zeile:
                    textfeld.insert("end", zeile, "einnahme")
                elif "| -" in zeile:
                    textfeld.insert("end", zeile, "ausgabe")
                else:
                    textfeld.insert("end", zeile)
    except FileNotFoundError:
        textfeld.insert("1.0", "Noch keine Datei gespeichert.")

# --- Hauptfenster ---
root = tk.Tk()
root.title("Budgetverwaltung")
root.geometry(f"{START_BREITE}x{START_HOEHE}")

def min_groesse(event):
    breite = root.winfo_width()
    hoehe = root.winfo_height()
    if breite < START_BREITE or hoehe < START_HOEHE:
        root.geometry(f"{max(breite, START_BREITE)}x{max(hoehe, START_HOEHE)}")
root.bind("<Configure>", min_groesse)

# --- Eingabefelder ---
frame_eingabe = ttk.Frame(root)
frame_eingabe.pack(pady=10)

ttk.Label(frame_eingabe, text="Betrag:").grid(row=0, column=0, padx=5, pady=5)
entry_betrag = ttk.Entry(frame_eingabe)
entry_betrag.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_eingabe, text="Beschreibung:").grid(row=1, column=0, padx=5, pady=5)
entry_beschreibung = ttk.Entry(frame_eingabe)
entry_beschreibung.grid(row=1, column=1, padx=5, pady=5)

# --- Kategorien (Radiobuttons) ---
kategorie_var = tk.StringVar(value="Keine Kategorie")
frame_kategorien = ttk.Frame(root)
frame_kategorien.pack(pady=5)
ttk.Radiobutton(frame_kategorien, text="Fixkosten", value="Fixkosten", variable=kategorie_var).pack(side="left")
ttk.Radiobutton(frame_kategorien, text="Lebensmittel", value="Lebensmittel", variable=kategorie_var).pack(side="left")
ttk.Radiobutton(frame_kategorien, text="Freizeit", value="Freizeit", variable=kategorie_var).pack(side="left")
ttk.Radiobutton(frame_kategorien, text="Sonstiges", value="Sonstiges", variable=kategorie_var).pack(side="left")

# --- Buttons für Buchungen ---
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=5)
btn_einnahme = ttk.Button(frame_buttons, text="Einnahme hinzufügen", command=einnahme_hinzufuegen)
btn_einnahme.grid(row=0, column=0, padx=5)
btn_ausgabe = ttk.Button(frame_buttons, text="Ausgabe hinzufügen", command=ausgabe_hinzufuegen)
btn_ausgabe.grid(row=0, column=1, padx=5)

# --- Listbox für Buchungen ---
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# --- Untere Buttons ---
frame_unten = ttk.Frame(root)
frame_unten.pack(pady=5)
btn_clear = ttk.Button(frame_unten, text="Clear", command=clear_liste)
btn_clear.grid(row=0, column=0, padx=5)
btn_speichern = ttk.Button(frame_unten, text="Speichern", command=speichern)
btn_speichern.grid(row=0, column=1, padx=5)
btn_oeffnen = ttk.Button(frame_unten, text="Liste", command=datei_oeffnen)
btn_oeffnen.grid(row=0, column=2, padx=5)

# --- Übersicht ---
label_uebersicht = tk.Label(root, text="Gesamteinnahmen: 0.00 €\nGesamtausgaben: 0.00 €\nSaldo: 0.00 €", font=("Segoe UI Emoji", 10))
label_uebersicht.pack(pady=10)

root.mainloop()