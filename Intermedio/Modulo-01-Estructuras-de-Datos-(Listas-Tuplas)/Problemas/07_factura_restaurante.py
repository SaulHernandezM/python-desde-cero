"""
Problema: La Factura de Restaurante (Tuplas y Listas)
Vamos a mezclar ambos conceptos. Las tuplas suelen usarse para representar "objetos" dentro de una lista.
    Crea una lista llamada pedido que contenga 3 tuplas. Cada tupla representa un plato: (nombre, precio).
    Ejemplo: [("Pizza", 12.5), ("Soda", 2.0), ("Helado", 4.5)]
    Lógica:
        Usa un bucle for para recorrer la lista de pedidos.
        En cada vuelta, desempaqueta la tupla en las variables nombre y precio.
        Imprime: "Plato: [nombre] ------ $[precio]".
        Reto Extra: Crea una variable total fuera del bucle y ve sumando los precios para mostrar 
        el total de la cuenta al final.
"""

pedido = [("Pizza", 12.5), ("Soda", 2.0), ("Helado", 4.5)]
total = 0

for nombre, precio in pedido:
    print(f"Plato: {nombre} ------- ${precio}.")
    total += precio

print(f"Total de la cuenta ${total}.")

