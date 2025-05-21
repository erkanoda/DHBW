Auswahl = input("Erdgas, Heizöl oder Strom? ")  
energie = float(input("Geben Sie die Energie in kwh ein: "))


def Auswahl():
    if "Erdgas":
        tarif = 0.09
    elif "Heizöl":
        tarif = 0.07    
    elif "Strom":
        tarif = 0.30
    auswahl = input("Ihre Wahl:")
    return Auswahl


def energiekosten(energie, tarif):
    kosten = energie * tarif
    return kosten
print(energiekosten(energie, Auswahl))
