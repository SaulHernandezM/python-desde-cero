"""
Reto: El Analista de Inventario
Imagina que tienes una lista de precios, pero en Python (por ahora) la trataremos 
como una serie de entradas.
    Pide al usuario cuántos productos desea registrar (ej: 3).
    Usa un for que se repita exactamente esa cantidad de veces usando range().
    Dentro del bucle:
        Pide el precio del producto.
        Si el precio es mayor a 100, súmalo a un acumulador llamado productos_caros.
        Si es menor o igual a 100, súmalo a productos_baratos.
    Al final: Muestra cuánto dinero gastarías en cosas caros y cuánto en cosas baratas por separado.
"""

numero_productos = int(input("Cantidad de productos a registrar: ")) 
productos_caros = 0
productos_baratos = 0

for productos in range(numero_productos):
    precio_producto = float(input(f"Precio del producto {productos + 1}: "))
    
    if precio_producto > 100:
        productos_caros += precio_producto
    
    else:
        productos_baratos += precio_producto
        
print(f"Dinero en productos con un precio mayor a 100: {productos_caros}")
print(f"Dinero en productos con un precio menor a 100: {productos_baratos}")
    
    
    
    

