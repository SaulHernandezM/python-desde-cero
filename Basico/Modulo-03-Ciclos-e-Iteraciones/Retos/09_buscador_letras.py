"""
Reto: El Buscador de Letras y Posiciones (Uso de for)
Este reto mezcla el recorrido de textos con contadores de posición.
    Pide al usuario una frase.
    Pide al usuario una letra específica que desee buscar.
    Lógica: Usa un bucle for para recorrer la frase.
        El programa debe decir en qué índice (posición) se encontró la letra.
        Extra: Al final, debe decir el total de veces que apareció esa letra.
    Ejemplo de salida: "Letra encontrada en la posición 2"
        "Letra encontrada en la posición 8"
        "Total de apariciones: 2"
"""

apariciones_letra = 0

frase_user = input("Ingrese una frase: ").strip().lower()
letra_espe = input("Ingrese una letra especifica a buscar: ").strip().lower()

for letra_espe in frase_user:
    if letra_espe in len(frase_user):
        apariciones_letra += 1
        
    
#print(f"Letra encontrada en la posicion {}.")
print(f"Total de apariciones {apariciones_letra}.")



