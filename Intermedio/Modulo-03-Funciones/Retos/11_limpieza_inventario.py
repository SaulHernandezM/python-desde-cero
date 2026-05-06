"""
Reto: Limpieza de Inventario (Eliminación)
Tu tienda ha decidido dejar de vender productos de baja calidad o agotados.
    Crea un diccionario inventario donde la llave es el producto y el valor es otro diccionario 
    con stock y calificacion.
        inventario = {"Teclado": {"stock": 0, "calif": 4}, "Mouse": {"stock": 10, "calif": 2}, 
        "Monitor": {"stock": 5, "calif": 5}}
    Misión: Crea una función limpiar_tienda(dicc_inv).
    Lógica: La función debe eliminar del inventario cualquier producto que cumpla cualquiera de 
    estas condiciones:
        El stock es 0.
        La calif (calificación) es menor a 3.
    Pista: No puedes borrar elementos de un diccionario mientras lo recorres con un for directamente. 
    Te sugiero crear una lista con las "llaves a borrar" y luego borrarlas fuera del bucle usando 
    del dicc[llave].
"""

def limpiar_tienda(dicc_inv):
    list_dict = ()
    for producto, stock, calificacion in dicc_inv:
        if stock == 0 and calificacion < 3:
            list_dict.append(producto[stock][calificacion])
        else:
            print("Condicion no cumplida.")
            
    if list_dict in dicc_inv:
        dicc_inv.clear(list_dict)
    return dicc_inv
        

inventario = {"Teclado": {"stock": 0, "calif": 4}, "Mouse": {"stock": 10, "calif": 2}, 
        "Monitor": {"stock": 5, "calif": 5}}

print(limpiar_tienda(inventario))

