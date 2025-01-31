import customtkinter as ctk  # Importiere die Bibliothek für modernes Tkinter-Design
from tkinter import messagebox  # Importiere das Modul für Meldungsfenster

# Modernes Design für die Anwendung setzen
ctk.set_appearance_mode("dark")  # Verfügbare Modi: "light", "dark" oder "system"
ctk.set_default_color_theme("blue")  # Farbthema festlegen: "blue", "green", "dark-blue"

# Funktion zur Berechnung der Zinsen
def berechnen():
    try:
        # Eingaben aus den Feldern lesen und in die richtigen Typen umwandeln
        start = float(entry_startkapital.get())  # Startkapital als Dezimalzahl
        zins = float(entry_zins.get()) / 100  # Zinssatz in Dezimalform umwandeln (z. B. 5% -> 0.05)
        zeit = int(entry_zeit.get())  # Anlagedauer in Jahren
        rate = float(entry_rate.get())  # Monatliche Sparrate

        # Validierung der Eingaben: Werte dürfen nicht negativ oder ungültig sein
        if start < 0 or zins < 0 or zeit <= 0 or rate < 0:
            raise ValueError("Alle Eingaben müssen positive Werte sein!")

        # Initialisierung der Berechnungsvariablen
        amount = start  # Anfangskapital
        gesamt_einzahlungen = 0  # Gesamte eingezahlte Sparraten

        # Berechnung der Kapitalentwicklung über die Jahre
        for jahr in range(1, zeit + 1):  # Schleife über die Jahre
            for monat in range(1, 13):  # Schleife über die Monate
                amount += rate  # Monatliche Einzahlung
                gesamt_einzahlungen += rate  # Gesamt eingezahltes Geld summieren
            
            amount *= (1 + zins)  # Jährliche Verzinsung anwenden

        # Berechnung des reinen Gewinns (ohne Einzahlungen)
        bereinigter_gewinn = amount - (start + gesamt_einzahlungen)

        # Ergebnis im Label anzeigen
        ergebnis_label.configure(
            text=f"\U0001F4CA Ergebnis nach {zeit} Jahren:\n" 
                 f"\U0001F3E6 Startkapital: {start:,.2f} €\n"               
                 f"\U0001F4B5 Gesparte Summe: {gesamt_einzahlungen:,.2f} €\n"
                 f"\U0001F4B0 Endkapital: {amount:,.2f} €\n"
                 f"\U0001F4C8 Gewinn: {bereinigter_gewinn:,.2f} €",
            font=("Arial", 14),
            fg_color="lightgrey",  # Hintergrundfarbe des Labels
            text_color="black",  # Textfarbe des Labels
            justify="left"  # Linksbündige Darstellung
        )
    except ValueError as e:
        # Falls eine ungültige Eingabe gemacht wurde, wird eine Fehlermeldung angezeigt
        messagebox.showerror("Fehler", f"Ungültige Eingabe: {e}")

# Hauptfenster erstellen
app = ctk.CTk()
app.title("Zinsrechner mit CustomTkinter")  # Titel des Fensters setzen
app.geometry("400x550")  # Fenstergröße definieren

# Labels und Eingabefelder für die Nutzereingabe
ctk.CTkLabel(app, text="Startkapital (€):").pack(pady=5)  # Beschriftung für Startkapital
entry_startkapital = ctk.CTkEntry(app, width=250)  # Eingabefeld für Startkapital
entry_startkapital.pack(pady=5)

ctk.CTkLabel(app, text="Zinssatz (% p.A.):").pack(pady=5)  # Beschriftung für Zinssatz
entry_zins = ctk.CTkEntry(app, width=250)  # Eingabefeld für Zinssatz
entry_zins.pack(pady=5)

ctk.CTkLabel(app, text="Anlagedauer (Jahre):").pack(pady=5)  # Beschriftung für Anlagedauer
entry_zeit = ctk.CTkEntry(app, width=250)  # Eingabefeld für Anzahl der Jahre
entry_zeit.pack(pady=5)

ctk.CTkLabel(app, text="Monatliche Sparrate (€):").pack(pady=5)  # Beschriftung für monatliche Sparrate
entry_rate = ctk.CTkEntry(app, width=250)  # Eingabefeld für Sparrate
entry_rate.pack(pady=5)

# Button zum Starten der Berechnung
btn_berechnen = ctk.CTkButton(app, text="Berechnen", command=berechnen)
btn_berechnen.pack(pady=10)

# Ergebnisfeld (optisch verbessert)
ergebnis_label = ctk.CTkLabel(
    app,
    text="",  # Anfangs leer
    fg_color="lightgrey",  # Hintergrundfarbe
    text_color="black",  # Textfarbe
    width=350,  # Breite des Ergebnislabels
    height=100,  # Höhe des Ergebnislabels
    font=("Arial", 14),  # Schriftart und -größe
    corner_radius=8,  # Abgerundete Ecken
    justify="center"  # Zentrierter Text
)
ergebnis_label.pack(pady=10)

# Tkinter Hauptloop starten (Hauptprogramm läuft in einer Endlosschleife)
app.mainloop()
