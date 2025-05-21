breite = float(input("Breite des Raumes in (m): "))
laenge = float(input("Länge des Raumes in (m): "))    
hoehe = float(input("Höhe des Raumes in (m): "))
t_innen = float(input("Innertemperatur in (°C): "))
t_aussen = float(input("Außentemperatur in (°C): "))

volumen  = breite * laenge * hoehe 

dt = t_innen - t_aussen

if dt < 0 :
    print("Achtung Temperaturdifferenz ist negativ") 

Heizlast = volumen * dt * 0.024
print("Die Heizlast beträgt: ", Heizlast, "kilo Watt")