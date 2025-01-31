import customtkinter as ctk
from tkinter import messagebox

# Modernes Design aktivieren
ctk.set_appearance_mode("dark")  # "light", "dark" oder "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# Funktion zur Berechnung der Zinsen
def berechnen():
    try:
        # Werte aus den Eingabefeldern holen
        start = float(entry_startkapital.get())
        zins = float(entry_zins.get()) / 100
        zeit = int(entry_zeit.get())
        rate = float(entry_rate.get())

        if start < 0 or zins < 0 or zeit <= 0 or rate < 0:
            raise ValueError("Alle Eingaben müssen positive Werte sein!")

        # Berechnung
        amount = start
        gesamt_einzahlungen = 0  

        for jahr in range(1, zeit + 1):
            for monat in range(1, 13):
                amount += rate  
                gesamt_einzahlungen += rate  
            
            amount *= (1 + zins)  # Jährliche Verzinsung

        # Bereinigter Gewinn berechnen
        bereinigter_gewinn = amount - (start + gesamt_einzahlungen)

        # Ergebnis anzeigen
        ergebnis_label.configure(
            text=f"📊 Ergebnis nach {zeit} Jahren:\n" 
                 f"🏦 Startkapital: {start:,.2f} €\n"               
                 f"💵 Gesparte Summe: {gesamt_einzahlungen:,.2f} €\n"
                 f"💰 Endkapital: {amount:,.2f} €\n"
                 f"📈 Gewinn: {bereinigter_gewinn:,.2f} €",
            font=("Arial", 14),
            fg_color="lightgrey",
            text_color="black",
            justify="left"
        )
    except ValueError as e:
        messagebox.showerror("Fehler", f"Ungültige Eingabe: {e}")

# Hauptfenster erstellen
app = ctk.CTk()
app.title("Zinsrechner mit CustomTkinter")
app.geometry("400x550")

# Labels und Eingabefelder
ctk.CTkLabel(app, text="Startkapital (€):").pack(pady=5)
entry_startkapital = ctk.CTkEntry(app, width=250)
entry_startkapital.pack(pady=5)

ctk.CTkLabel(app, text="Zinssatz (% p.A.):").pack(pady=5)
entry_zins = ctk.CTkEntry(app, width=250)
entry_zins.pack(pady=5)

ctk.CTkLabel(app, text="Anlagedauer (Jahre):").pack(pady=5)
entry_zeit = ctk.CTkEntry(app, width=250)
entry_zeit.pack(pady=5)

ctk.CTkLabel(app, text="Monatliche Sparrate (€):").pack(pady=5)
entry_rate = ctk.CTkEntry(app, width=250)
entry_rate.pack(pady=5)

# Berechnen-Button
btn_berechnen = ctk.CTkButton(app, text="Berechnen", command=berechnen)
btn_berechnen.pack(pady=10)

# Ergebnisfeld (optisch verbessert)
ergebnis_label = ctk.CTkLabel(
    app,
    text="",
    fg_color="lightgrey",
    text_color="black",
    width=350,
    height=100,
    font=("Arial", 14),
    corner_radius=8,
    justify="center"
)
ergebnis_label.pack(pady=10)

# Tkinter Hauptloop starten
app.mainloop()
