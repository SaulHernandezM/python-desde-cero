"""
Reto: El Contador de Espacios y Puntos
Este reto te ayudará a identificar caracteres específicos en una frase larga.
    Pide al usuario que escriba una frase (ej: "Hola. Soy Python.").
    Usa un bucle for para recorrer la frase.
    Lógica:
        El programa debe contar cuántos puntos . hay.
        El programa debe contar cuántos espacios " " hay.
    Al final: Muestra ambos totales por separado.
"""

frase = input("Ingrese una frase: ")

contador_punto = 0
contador_espacio = 0

for caracter in frase:
    if caracter == ".":
        contador_punto += 1
    elif caracter == " ":
        contador_espacio += 1

print(f"La frase: {frase}")
print(f"Contiene {contador_punto} puntos y {contador_espacio} espacios.")



