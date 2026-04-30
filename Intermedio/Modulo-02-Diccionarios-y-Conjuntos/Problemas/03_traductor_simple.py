"""
Problema: El Traductor Simple
Este ejercicio te enseñará a usar diccionarios para "mapear" o traducir información.
    Crea un diccionario llamado diccionario_colores donde las llaves estén en inglés y 
    los valores en español (ej: {"red": "rojo", "blue": "azul", "green": "verde"}).
    Lógica:
        Pide al usuario que escriba un color en inglés.
        Si el color está en el diccionario, imprime: "La traducción de [color] es [valor]".
        Si no está, imprime: "Ese color no se encuentra en mi base de datos".
    Extra: Muestra al usuario todos los colores que sí sabes traducir usando .keys().
"""

diccionario_colores = {"red": "rojo", "blue": "azul", "green": "verde", 
                       "orange": "naranja", "black": "negro", "white": "blanco"}

color = input("Color: ")

if color in diccionario_colores:
    print(f"La traduccion de {color} es {diccionario_colores[color]}")
else:
    print(f"El color {color} no se encuentra en la base de datos.")
    print(f"Colores traducidos: {diccionario_colores.keys()}.")