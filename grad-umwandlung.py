# Definition der Funktion zur Umrechnung von Celsius in Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

# Aufrufe der Funktion mit den gewünschten Werten 
celsius_1 = 25
celsius_2 = 10

# Ausgabe 
print(f"{celsius_1}°C in Fahrenheit: {celsius_to_fahrenheit(celsius_1)}°F")
print(f"{celsius_2}°C in Fahrenheit: {celsius_to_fahrenheit(celsius_2)}°F")

