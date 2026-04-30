"""
Problema: El Supermercado (Búsqueda y Eliminación)
Este ejercicio te ayudará a manejar elementos por su valor y no solo por su índice.
    Crea una lista llamada carrito con 5 productos (ej: "pan", "leche", "huevo", "manzana", "arroz").
    Muestra la lista al usuario.
    Pide al usuario que escriba el nombre de un producto que quiera eliminar del carrito.
    Lógica:
        Usa el operador in para verificar si el producto existe en la lista.
        Si existe, elimínalo usando .remove(nombre_del_producto).
        Si no existe, muestra un mensaje de "Producto no encontrado".
    Muestra la lista final.
"""
carrito = ["pan", "leche", "huevo", "manzana", "arroz"]

print(f"Su carrito contiene: {carrito}.")

eliminar_producto = input("Escribe el numbre del producto que desea eliminar: ")

if eliminar_producto in carrito:
    carrito.remove(eliminar_producto)
    print("Producto eliminado.")
    
else:
    print("Producto no encontrado.")
    
print(carrito)
    
    




