"""
Reto: El Auditor de Ventas (Listas + Diccionarios + Totales)
Este reto simula un reporte de ventas de un día.
    Crea un diccionario de precios (ej: {"Cafe": 30, "Galleta": 15, "Te": 25}).
    Crea una lista de ventas_del_dia que contenga solo los nombres de lo que se 
    vendió (ej: ["Cafe", "Te", "Cafe", "Galleta"]).
    Crea una función llamada generar_reporte(lista_ventas, dict_precios).
    Misión: La función debe recorrer la lista de ventas, buscar el precio de cada artículo 
    en el diccionario e ir sumando todo.
    Retorno: Debe retornar un nuevo diccionario con dos datos: 
    {"total_dinero": X, "cantidad_articulos": Y}.
    Uso: Llama a la función y muestra el reporte final de la caja.
"""

def generar_reporte(lista_ventas, dict_precios):
    suma = 0
    nuevo_dict = {}
    for lista_ventas in dict_precios:
        suma += dict_precios[lista_ventas]
        nuevo_dict.update(lista_ventas)
    return suma, nuevo_dict    
    
precios = {"Cafe": 30, "Galleta": 15, "Te": 25, "Pastel rebanada": 50, "Pay": 60, "Chocolate": 30}

ventas_dia = ["Cafe", "Galleta", "Pay", "Chocolate"]

reporte = generar_reporte(ventas_dia, precios)
print(f"Total dinero: {sum} | Cantidad articulos: {len(nuevo_dict)}")

"""
El Bucle Equivocado: Al hacer for lista_ventas in dict_precios:, le estás diciendo a Python que revise 
cada producto del menú una vez. Pero en la vida real, ¡puedes vender 10 cafés y ninguna galleta! Debes 
recorrer lista_ventas.

Uso de update: El método .update() sirve para fusionar dos diccionarios, no para agregar elementos sueltos.

El "Scope" (Alcance): Intentaste imprimir sum y nuevo_dict fuera de la función. Recuerda que lo que pasa 
en la función, se queda en la función... a menos que lo retornes y lo guardes en una variable nueva.
"""