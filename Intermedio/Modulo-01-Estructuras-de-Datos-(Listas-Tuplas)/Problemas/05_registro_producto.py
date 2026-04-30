"""
Problema: El Registro de Producto (Tuplas)
Las tuplas son ideales para datos que representan una "unidad" de 
información que no debe separarse.
    Crea una tupla llamada producto que contenga: "Laptop", 1500 (precio), y 
    "Electrónica" (categoría).
    Lógica:
        Intenta cambiar el precio a 1200 y observa el error en la terminal de 
        VS Code (luego comenta esa línea con # para que el código siga).
        Usa el Desempaquetado de Tuplas (investiga: nombre, precio, cat = tupla) 
        para extraer los datos en variables individuales.
    Imprime un mensaje: "El producto [nombre] cuesta $[precio] y pertenece a [cat]".
"""

producto = ("Laptop", 1500, "Electrónica")

nombre, precio, categoria = producto

print(f"El producto {nombre} cuesta ${precio} y pertenece a {categoria}.")

