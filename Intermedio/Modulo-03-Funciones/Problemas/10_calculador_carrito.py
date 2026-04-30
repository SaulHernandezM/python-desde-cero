"""
Problema: El Calculador de Carrito (Sumatorias)
Este ejercicio te enseñará a procesar una lista usando datos de un diccionario.
    Crea un diccionario llamado precios con 5 productos y sus costos.
    Crea una función llamada calcular_total(lista_compras, diccionario_precios).
    Misión: La función recibe una lista de nombres (ej: ["Pan", "Jugo"]) y debe buscar sus 
    precios en el diccionario para sumarlos.
    Retorno: El total de la compra.
    Uso: Define el diccionario, crea una lista de compras y muestra el total.
"""

precios = {"Huevo": 94., "Leche": 27., "Sabritas": 21., "Galletas": 20., "Gansito": 22., "Frijoles": 15.}

def calcular_total(lista_compras, diccionario_precios):
    suma_productos = 0
    for producto, costo in diccionario_precios.items():
        if lista_compras in producto:
            suma_productos += costo
    return suma_productos
    
compras = []

print(precios)
num_productos = int(input("Productos a comprar (1-n): "))

for x in range(1, num_productos + 1):
    producto = input("Nombre producto: ")
    compras.append(producto)
   
total_compra = calcular_total(compras, precios)
print(f"Productos comprados: {compras}.")
print(f"Total de la compra: {total_compra}.")     



"""
Tu error estuvo aquí: if lista_compras in producto:.
Lo que intentaste: ¿Está mi lista entera de compras dentro de la palabra "Huevo"?
La realidad: Python no puede meter una lista en un string. Lo que tú quieres es saber si el 
producto de la tienda está en tu lista de compras.
La solución: Es más fácil recorrer tu lista de compras y buscar el precio en el diccionario.
"""
      