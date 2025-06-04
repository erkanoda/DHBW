Auswahl = input("Erdgas, Heizöl oder Strom? ")  
energie = float(input("Geben Sie die Energie in kwh ein: "))

def konvert(a):
    if a == "Erdgas":
        tarif = 0.09
    elif a == "Heizöl":
        tarif = 0.07    
    elif a == "Strom":
        tarif = 0.30
    return tarif

def energiekosten(energie, tarif):
    kosten = energie * tarif
    return kosten
print(energiekosten(energie, konvert(Auswahl))) 

