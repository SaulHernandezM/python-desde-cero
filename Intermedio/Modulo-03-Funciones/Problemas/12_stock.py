"""
Problema: ¿Qué hay en Stock?
Este ejercicio te ayudará a filtrar datos basados en sus valores.
Crea un diccionario llamado inventario donde las llaves sean productos y los valores sean la 
cantidad disponible (ej: {"Manzanas": 50, "Peras": 0, "Uvas": 10}).
Crea una función llamada productos_agotados(dicc_stock).
Misión: La función debe recorrer el inventario y retornar una lista con los nombres de los 
productos que tengan cantidad igual a 0.
Uso: Imprime la lista de productos que el dueño de la tienda debe volver a comprar.
"""

inventario = {"Manzanas": 50, "Peras": 0, "Uvas": 10, "Melones": 15, "Sandias": 10, "Platanos": 0, 
              "Naranjas": 70, "Guayabas": 0, "Jicamas": 10, "Pepinos": 10, "Ciruelas": 0}

def productos_agotados(dicc_stock):
    producto_cero = []
    for producto, stock in dicc_stock.items():
       # if dicc_stock[stock] == 0:
           # producto_cero.append(dicc_stock[producto])
        if stock == 0: # stock ya es el número, no necesitas entrar al dicc de nuevo
            producto_cero.append(producto) # Guardamos el nombre
    return producto_cero

sin_stock = productos_agotados(inventario)

print(f"Productos sins stock: {sin_stock}.")


"""
En tu código escribiste: if dicc_stock[stock] == 0:.
El Error: Cuando haces for producto, stock in dicc_stock.items(), la variable stock ya es el 
número (ej. 50, 0, 10). Al poner dicc_stock[stock], le estás diciendo a Python: "Busca un producto 
que se llame '0'". Como no hay ningún producto llamado "0", el programa falla.
La Solución: ¡Ya tienes el dato! Solo tienes que preguntar if stock == 0:.
Otro detalle: En el append pusiste dicc_stock[producto], eso guardaría el número 0. Queremos 
el nombre del producto, así que solo ponemos producto.
"""



