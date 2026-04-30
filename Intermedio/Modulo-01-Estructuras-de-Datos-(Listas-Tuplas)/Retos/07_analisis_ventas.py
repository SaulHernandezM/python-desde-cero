"""
Reto: Análisis de Ventas (Tuplas)
Las tuplas son perfectas para registros históricos que no deben ser alterados.
    Crea una lista llamada ventas_dia que contenga tuplas con el formato (producto, cantidad, precio_unitario).
    Ejemplo: [("Cafe", 2, 2.5), ("Pan", 5, 1.2), ("Jugo", 1, 3.0)].
    Misión: Recorre la lista y, por cada tupla:
        Calcula el subtotal (cantidad * precio).
        Imprime: "Venta: [producto] | Total: $[subtotal]".
    Final: Muestra el Gran Total de todas las ventas del día.
"""

ventas_dia = [("Cafe", 2, 100.99), ("Pan", 5, 6.), ("Jugo", 3, 24.5),
              ("Leche", 9, 27.), ("Avena", 4, 33.90), ("Sabritas", 5, 50.)]

suma_productos = 0

for producto, cantidad, precio_unitario in ventas_dia:
    subtotal = (cantidad * precio_unitario)
    suma_productos += subtotal
    print(f"Venta: {producto} | Total: ${subtotal}.")

print(f"Total: ${suma_productos}.")