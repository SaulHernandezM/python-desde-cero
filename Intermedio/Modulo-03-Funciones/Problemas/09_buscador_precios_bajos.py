"""
Problema: El Buscador de Precios Bajos (Dics + Funciones)
Vamos a usar una función para filtrar datos complejos.
    Crea una función llamada buscar_baratos(productos, presupuesto).
        productos será un diccionario como: {"Pan": 1.5, "Leche": 2.0, "Carne": 15.0}.
        presupuesto será un número.
    Misión: La función debe retornar una lista con los nombres de los productos que cuesten menos 
    o igual que el presupuesto.
    Uso: Define el diccionario de productos, pide el presupuesto al usuario y muestra la lista resultante.
"""

def buscar_baratos(productos, presupuesto):
    productos_presupuesto = []
    for precio in productos:
        if precio <= productos:
            productos_presupuesto.append(precio)
        return productos_presupuesto
            

productos = {"Pan": 7., "Leche": 27., "Carne": 124.5, "Huevos": 94.5, "Cereal": 90., "Jugo": 24.}

usuario_presupuesto = float(input("Presupuesto: "))

productos_disponibles = buscar_baratos(productos, usuario_presupuesto)

print(f"Productos disponibles en base a su presupuesto: {productos_disponibles}.")

"""
Problemas
Iteración de llaves: Por defecto, un for en un diccionario recorre las llaves. Así que estabas 
comparando "Pan" <= {...}.
Comparación lógica: Para acceder al precio, debes usar la llave dentro del diccionario: productos[nombre].
La posición del return: Lo pusiste dentro del for. Como vimos antes, esto hace que la función se detenga
en el primer producto ("Pan") y no revise los demás.
"""
