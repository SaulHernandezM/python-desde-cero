"""
Reto: Historial de Precios (Diccionarios con Listas de Flotantes)
    Crea un diccionario productos donde la llave es el nombre del artículo y el valor es una 
    lista de sus precios en los últimos 3 meses.
        {"Pan": [10.5, 11.0, 10.8], "Agua": [15.0, 15.0, 16.0]}
    Crea una función llamada detectar_inflacion(dicc_precios).
    Misión: La función debe devolver una lista con los nombres de los productos cuyo último precio 
    sea mayor que el primer precio de la lista.
    Concepto clave: Uso de índices negativos lista[-1] vs lista[0].
"""

def detectar_inflacion(dicc_precios):
    productos_precio = []
    
    for producto, precios in dicc_precios.items():
        if precios[0] < precios[-1]:
            productos_precio.append(producto)
        
    return  productos_precio

productos = {"Pan": [10.5, 11.0, 10.8], "Agua": [15.0, 15.0, 15.0], "Arroz": [14.0, 13.0, 16.0],
             "Frijol": [11.0, 11.0, 13.0], "Jugo": [17.0, 12.0, 16.0], "Sal": [7.0, 6.0, 6.0]}

producto_cumple = detectar_inflacion(productos)

print(producto_cumple)

