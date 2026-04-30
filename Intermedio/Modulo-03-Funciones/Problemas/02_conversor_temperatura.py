"""
Problema: El Conversor de Temperatura
Las funciones son ideales para fórmulas matemáticas que no queremos escribir mil veces.
    Crea una función llamada celsius_a_fahrenheit que reciba los grados Celsius y retorne el resultado.
        Fórmula: (Celsiusx1.8)+32
    Pide al usuario la temperatura en Celsius, llama a la función e imprime el resultado final.
"""

def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32


print("#### Celsius a Fahrenheit ####")
celsius = float(input("Celsius: "))

print(f"Conversion a Fahrenheit: {celsius_a_fahrenheit(celsius)}.")
