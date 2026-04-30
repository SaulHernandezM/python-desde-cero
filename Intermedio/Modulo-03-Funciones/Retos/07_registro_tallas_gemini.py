"""
Reto: El Registro de Tallas (Diccionario de Diccionarios)
Vamos a crear una base de datos para una tienda de zapatos.
    Crea una función registrar_zapato(almacen, modelo, talla, cantidad).
    Misión: La función recibe un diccionario almacen (que puede estar vacío al inicio). Debe organizar 
    todo de forma que el modelo sea la llave principal y su valor sea otro diccionario de tallas.
        Estructura deseada: {"Nike Air": {38: 5, 40: 2}, "Adidas Run": {39: 10}}
    Lógica: Si el modelo no existe, créalo con su diccionario de tallas.
        Si el modelo existe pero la talla no, agrega la talla.
        Si ambos existen, suma la cantidad a la que ya había.
"""

def registrar_zapato(almacen, modelo, talla, cantidad):
    # Paso 1: ¿Existe el modelo?
    if modelo not in almacen:
        almacen[modelo] = {} # Creamos el diccionario interno para las tallas
    
    # Paso 2: ¿Existe la talla dentro de ese modelo?
    if talla in almacen[modelo]:
        almacen[modelo][talla] += cantidad
    else:
        almacen[modelo][talla] = cantidad
        
    return almacen

# Prueba
stock = {}
registrar_zapato(stock, "Nike Air", 40, 5)
registrar_zapato(stock, "Nike Air", 40, 2) # Suma a la misma talla
registrar_zapato(stock, "Adidas Run", 39, 10)

print(f"Almacén actualizado: {stock}")
    