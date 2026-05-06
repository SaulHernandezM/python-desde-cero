def limpiar_tienda(dicc_inv):
    # No podemos borrar mientras recorremos, así que anotamos quiénes se van
    productos_a_eliminar = []
    
    for producto, info in dicc_inv.items():
        # Accedemos al diccionario interno 'info'
        if info["stock"] == 0 or info["calif"] < 3:
            productos_a_eliminar.append(producto)
            
    # Ahora que terminamos de revisar, borramos de verdad
    for producto in productos_a_eliminar:
        del dicc_inv[producto]
        
    return dicc_inv


inventario = {"Teclado": {"stock": 0, "calif": 4}, "Mouse": {"stock": 10, "calif": 2}, 
        "Monitor": {"stock": 5, "calif": 5}}

print(limpiar_tienda(inventario))