"""
Reto: El Auditor de Precios (Listas)
Este reto te obligará a comparar elementos de una lista para tomar decisiones globales.
    Pide al usuario que ingrese 8 precios de productos y guárdalos en una lista.
    Misión: Una vez llena la lista, el programa debe:
        Calcular el precio promedio.
        Crear una nueva lista llamada precios_altos que contenga solo los precios que superen el promedio.
    Salida: Muestra el promedio y la lista de los precios que son "más caros que el promedio".
"""

productos = []

print("#### Ingresa 8 precios de productos ####")

for x in range(1, 9):
    ingresar_producto = int(input(f"Producto {x}: "))
    productos.append(ingresar_producto)
    
promedio = sum(productos) / len(productos)
precios_altos = []

for precio in productos:
    if precio > promedio: 
        precios_altos.append(precio)

print(f"Promedio: ${promedio}.")
print(f"Precios mas caros: {precios_altos}.")

