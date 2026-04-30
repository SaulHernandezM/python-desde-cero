"""
Problema: El Filtro de Precios (Filtrado con Bucle)
    Crea un diccionario llamado productos con nombres y precios 
    (ej: {"Leche": 20, "Pan": 10, "Vino": 50}).
    Crea una función llamada filtrar_por_precio(diccionario, precio_maximo).
    Misión: La función debe recorrer el diccionario y retornar una lista con 
    los nombres de los productos que cuesten menos que el precio_maximo.
    Uso: Pide al usuario su presupuesto y muéstrale qué puede comprar.
"""

def filtrar_por_precio(diccionario, precio_maximo):
    productos_presupuesto = []
    for producto, costo in diccionario.items():
        if producto in diccionario:
            if costo < precio_maximo:
                productos_presupuesto.append(producto)
        else:
            return "Producto no encontrado."
        
    return productos_presupuesto

productos_tienda = {"Leche": 27., "Pan": 7., "Vino": 104.5, "Cerveza": 20., 
             "Refresco": 20., "Carne": 120.5}


presupuesto = float(input("Presupuesto: "))

productos_disponibles = filtrar_por_precio(productos_tienda, presupuesto)

print(f"Productos que puede comprar: {productos_disponibles}.")


"""
Tu lógica de filtrado es correcta, pero tienes una redundancia. Dentro del for, 
preguntaste if producto in diccionario. Esto es como estar dentro de tu casa y 
preguntarte: "¿Estoy en mi casa?". Como el for ya está sacando los productos del diccionario, 
esa condición siempre será verdadera.
"""
