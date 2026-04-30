"""
Reto: El Catálogo de Películas (Filtro en Listas de Diccionarios)
Este reto simula un motor de búsqueda de streaming.
    Crea un diccionario cine. Las llaves son géneros ("Accion", "Drama"). 
    El valor es una lista de diccionarios, cada uno con titulo y año.
        {"Accion": [{"titulo": "John Wick", "año": 2014}, {"titulo": "Mad Max", "año": 2015}]}
    Misión:
        Pide al usuario un género.
        Si existe, pide un año mínimo (ej. 2015).
        Recorre la lista de ese género y muestra solo las películas que se hayan estrenado 
        en ese año o después.
        Si ninguna cumple, avisa al usuario.
"""

cine = {"Accion": [{"titulo": "John Wick", "año": 2014}, {"titulo": "Mad Max", "año": 2015}],
        "Drama": [{"titulo": "Romeo y Julieta", "año": 2004}, {"titulo": "La isla de las tentaciones", "año": 2010}]}

user_genero = input("Genero (Accion, Drama): ")

if user_genero in cine:
    año_pelicula = int(input("Año minimo (ej. 1990): "))
    for titulo_p, año_estreno in cine[user_genero]:
        if año_pelicula >= año_estreno:
            titulo = titulo_p["titulo"]
            año = año_estreno[año]
            print(f"Pelicula: {titulo} | Año de estreno: {año}.")    
else:
    print("Genero no disponible.")
    
    
"""
for variable1, variable2 in lista_de_diccionarios:.
El error: Python solo puede "desempaquetar" así si la lista contiene tuplas de dos elementos 
(como vimos en el reto de los vuelos).
La realidad: Tu lista contiene Diccionarios. Por lo tanto, el bucle for solo puede tomar un objeto
a la vez (el diccionario completo).
"""
