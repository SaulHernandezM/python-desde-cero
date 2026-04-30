"""
Reto: El Monitor de Vuelos (Tuplas + Listas)
Este reto simula un panel de información en un aeropuerto.
    Crea una lista llamada vuelos que contenga al menos 4 tuplas. Cada tupla representa un vuelo: 
    (NumeroVuelo, Destino, Estado).
    Ejemplo: [("AR123", "Madrid", "A tiempo"), ("MX456", "Cancún", "Retrasado"), ...]
    Requerimientos del Sistema:
        Pide al usuario que ingrese un Destino para buscar.
        Usa un bucle for para recorrer la lista y desempaquetar las tuplas.
        Lógica de Filtrado: Si el destino coincide con el que ingresó el usuario, imprime: 
        "Vuelo [NumeroVuelo] con destino a [Destino] se encuentra [Estado]".
        Si el destino no coincide con ningún vuelo, al finalizar el bucle el programa debe 
        avisar que no se encontraron vuelos para ese lugar.
"""

vuelos =  [("AR123", "Madrid", "A tiempo"), ("MX456", "Cancún", "Retrasado"), 
           ("MX943", "Acapulco", "Retrasado"), ("MX343", "Queretaro", "A tiempo")]

buscar_destino = input("Ingrese un destino: ").strip()
encontrado = False

for numeroVuelo, destino, estado in vuelos:
    
    # Comparamos el input directamente con la variable 'destino' desempaquetada
    #if buscar_destino == destino:
    
    if buscar_destino in vuelos:
        print(f"Vuelo {numeroVuelo} con destino a {destino} se encuentra {estado}.")
        encontrado = True

if not encontrado:
    print("No se encontraron vuelos para ese lugar.")        
        

"""
En tu código escribiste: if buscar_destino in vuelos:.
    vuelos es una lista que contiene tuplas, no palabras sueltas.
    Si tú buscas "Madrid", Python mira dentro de la lista y pregunta: 
    "¿Es 'Madrid' igual a la tupla ('AR123', 'Madrid', 'A tiempo')?". La respuesta es False.
    La solución: Como ya hiciste el desempaquetado en el for (for numeroVuelo, destino, estado in vuelos:), 
    ya tienes la variable destino limpia y lista para comparar.
"""