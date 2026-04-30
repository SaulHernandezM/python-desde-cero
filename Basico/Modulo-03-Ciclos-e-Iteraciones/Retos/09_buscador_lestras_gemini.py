frase = input("Frase: ").lower()
objetivo = input("Letra a buscar: ").lower()

posicion = 0  # Contador manual de posición
apariciones = 0

# El 'for' recorre la frase letra por letra
for letra_actual in frase:
    if letra_actual == objetivo:
        print(f"Letra encontrada en la posición {posicion}")
        apariciones += 1
    
    # IMPORTANTE: En cada vuelta, sin importar si encontramos la letra o no,
    # sumamos 1 a la posición para saber en qué letra vamos.
    posicion += 1

print(f"Total de apariciones: {apariciones}")