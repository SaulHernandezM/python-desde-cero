"""
Problema: El Traductor de Frutas (Diccionarios)
Este ejercicio te enseñará a manejar diccionarios para validaciones rápidas.
    Crea un diccionario llamado frutas_precios con 4 frutas y sus precios.
    Misión: Pide al usuario el nombre de una fruta.
        Si la fruta está en el diccionario, imprime: "La fruta [nombre] cuesta $[precio]".
        Si no está, pregunta al usuario: "¿Deseas agregarla? (S/N)".
        Si el usuario dice "S", pide el precio y agrégala. Si dice "N", despídete.
    Al final, muestra cuántos productos totales tiene tu tienda usando len().
"""

frutas_precios = {"manzana": 10, "pera": 15, "durazno": 20, "uvas": 44, 
                  "piña": 30, "sandia": 40, "jicama": 24, "guayaba": 5}

nombre_fruta = input("Nombre fruta: ").lower()

if nombre_fruta in frutas_precios:
    print(f"La fruta {nombre_fruta} cuestas ${frutas_precios[nombre_fruta]}")
else:
    agregar_fruta = input("Fruta no encontrada, ¿Deseas agregarla? (S/N): ").lower()
    if agregar_fruta == "s":
        precio = int(input("Precio: "))
        frutas_precios[nombre_fruta] = precio
        print(f"Fruta: {nombre_fruta}. | Precio: {precio}. Agregada.")
    else:
        print("Adios.")
            
print("Productos en tienda:",len(frutas_precios))

