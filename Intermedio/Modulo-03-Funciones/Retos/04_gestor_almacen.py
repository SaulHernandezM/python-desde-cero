"""
Reto: El Gestor de Almacén (Modificación + Retorno de Tuplas)
Este reto te obligará a actualizar datos y devolver múltiples resultados.
    Crea un diccionario inventario con productos y sus cantidades (ej: {"Manzanas": 10, "Peras": 5}).
    Crea una función llamada actualizar_y_revisar(producto, cantidad_vendida, dicc).
    Misión:
        La función debe restar la cantidad_vendida al stock del producto.
        Debe retornar una tupla con dos valores: el nuevo stock y un booleano que sea True si el 
        stock bajó de 3 (alerta de reabastecimiento), o False si aún hay suficiente.
    Uso: Llama a la función y muestra un mensaje: "Nuevo stock de [producto]: [n]. 
    ¿Necesita reabastecer?: [Si/No]".
"""

def actualizar_y_revisar(producto, cantidad_vendida, dicc):
    for producto, stock in dicc:
        productos[producto] = cantidad_vendida - stock
        
        nuevo_stock = (
            "Nuevo stock": productos[producto],
            if productos[producto] < 3:
                return True
            else:
                return False
        )
        
        return nuevo_stock
        
    if not producto in dicc:
        return "Fruta no encontrada."


productos = {"Manzanas": 20, "Peras": 15, "Calabaza": 10, "Uvas": 25, "Naranjas": 40,
             "Pepinos": 14, "Platanos": 44, "Jicamas": 8, "Fresas": 50, "Arandanos": 60}


user_producto = input("Producto: ")
user_cantidad = int(input("Cantidad Vendida: "))

actualizar = actualizar_y_revisar(user_cantidad, user_cantidad, productos)

print(f"Nuevo stock de {user_producto}: {actualizar["Nuevo stock"]}")
print(f"¿Necesita reabastecer?: ")


"""
El Bucle Innecesario: Al hacer for producto, stock in dicc:, Python se confunde porque para usar 
.items() necesitas especificarlo. Además, si ya tienes el nombre del producto, no necesitas recorrer
toda la tienda.

Sintaxis de Tupla: Las tuplas no llevan etiquetas como los diccionarios (ej: "Nuevo stock": ...). Son 
solo valores separados por comas: (valor1, valor2).

Lógica Inversa: Escribiste cantidad_vendida - stock. Si tengo 20 manzanas y vendo 5, la cuenta es 20−5. 
Tu código estaba haciendo 5−20, lo que te daría un stock de −15.

Llamada a la función: Al final, pasaste user_cantidad dos veces en lugar de pasar el nombre del producto.
"""