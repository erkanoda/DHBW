celsius = float(input("Geben Sie die Temperatur in Celsius ein: "))

def celsius_to_kelvin(celsius):
    Kelvin = celsius + 273.15
    return Kelvin 
print(celsius_to_kelvin(celsius))   
   

def celsius_to_fahrenheit(celsius):
    Fahrenheit = (celsius * 9/5) + 32
    return  Fahrenheit
print(celsius_to_fahrenheit(celsius))   

