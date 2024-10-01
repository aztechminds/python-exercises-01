# Definition der Funktion zur Berechnung des Preises inklusive Mehrwertsteuer. 
def price_with_tax(preis):
    steuer_rate = 0.19 # Mehrwertsteuer von 19%
    gesamtpreis = preis * (1 + steuer_rate)
    return gesamtpreis

# Aufruf der Funktion mit den gewünschten Artikelpreisen
artikel_preis_1 = 99.99
artikel_preis_2 = 1.99

# Ausgabe
print(f"Preis inkl. 19% MwSt für 99,99 EURO: {price_with_tax(artikel_preis_1):.2f} Euro")
print(f"Preis inkl. 19% MwSt für 1,99 Euro: {price_with_tax(artikel_preis_2):.2f} Euro")
