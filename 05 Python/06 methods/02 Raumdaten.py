def eingabe_der_Werte():
    breite = float(input("Breite in m: "))
    laenge = float(input("Länge in m: "))
    hoehe = float(input("Höhe in m: "))
    t_innen = float(input("Innertemperatur in °C: "))
    t_aussen = float(input("Außentemperatur in °C: "))

    volumen  = breite * laenge * hoehe  
    dt = t_innen - t_aussen
    return volumen, dt

volumen, dt = eingabe_der_Werte()

def berechnen(volumen, dt):
    Heizlast = volumen * dt * 0.024
    return Heizlast

if dt < 0 :
    print("Achtung Temperaturdifferenz ist negativ") 

Heizlast = berechnen(volumen, dt)    
print("Die Heizlast beträgt: ", Heizlast, "kilo Watt")