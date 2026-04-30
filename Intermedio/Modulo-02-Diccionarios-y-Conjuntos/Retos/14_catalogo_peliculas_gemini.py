cine = {
    "Accion": [{"titulo": "John Wick", "año": 2014}, {"titulo": "Mad Max", "año": 2015}],
    "Drama": [{"titulo": "Romeo y Julieta", "año": 2004}, {"titulo": "La isla", "año": 2010}]
}

genero = input("Género: ")
if genero in cine:
    anio_min = int(input("Año mínimo: "))
    encontrado = False
    
    # 'peli' será cada diccionario: {"titulo": "...", "año": ...}
    for peli in cine[genero]:
        if peli["año"] >= anio_min: # Comparamos el año de la peli vs el pedido
            print(f"-> {peli['titulo']} ({peli['año']})")
            encontrado = True
            
    if not encontrado:
        print("No hay películas tan recientes en este género.")