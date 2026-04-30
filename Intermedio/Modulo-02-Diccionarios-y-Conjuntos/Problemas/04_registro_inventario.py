"""
Problema: Registro de Inventario (Diccionarios)
Este ejercicio simula el control de stock de una tienda.
    Crea un diccionario llamado stock con 3 productos y su cantidad actual 
    (ej: {"camisas": 10, "pantalones": 5, "zapatos": 8}).
    Lógica:
        Pide al usuario el nombre de un producto.
        Si el producto existe, pregunta: "¿Cuántas unidades nuevas llegaron?". Suma esa 
        cantidad al valor actual en el diccionario.
        Si el producto no existe, pregunta su cantidad inicial y agrégalo como un nuevo 
        registro al diccionario.
    Al final, imprime el inventario completo usando un bucle for producto, 
    cantidad in stock.items():.
"""

stock = {"camisas": 10, "pantalones": 5, "zapatos": 8}

nombre_producto = input("Nombre Producto: ")
if nombre_producto in stock:
    unidades = int(input("Cuantas unidades llegaron?: "))
    unidades += stock[nombre_producto]

else:
    unidades = int(input("Cuantas unidades llegaron?: "))
    stock[nombre_producto] = unidades

for nombre_producto, unidades in stock.items():
    print(f"Producto: {stock[nombre_producto]}. Cantidad: {stock[unidades]}.")


