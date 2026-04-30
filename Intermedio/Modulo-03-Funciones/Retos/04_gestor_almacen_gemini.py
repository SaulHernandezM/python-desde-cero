def actualizar_y_revisar(producto, cantidad_vendida, dicc):
    # 1. Buscamos directamente sin bucles
    if producto in dicc:
        # 2. Restamos al valor original: $$Stock_{final} = Stock_{inicial} - Venta$$
        dicc[producto] -= cantidad_vendida
        nuevo_stock = dicc[producto]
        
        # 3. Creamos la alerta booleana
        necesita_reabastecer = nuevo_stock < 3
        
        # 4. Retornamos la tupla (número, booleano)
        return (nuevo_stock, necesita_reabastecer)
    else:
        return None # Retornamos algo que indique que no existe

productos = {
    "Manzanas": 20, "Peras": 15, "Calabaza": 10, "Uvas": 25, 
    "Naranjas": 40, "Pepinos": 14, "Platanos": 44, "Jicamas": 8, 
    "Fresas": 5, "Arandanos": 60
}

user_prod = input("Producto: ").strip().capitalize()
user_cant = int(input("Cantidad Vendida: "))

resultado = actualizar_y_revisar(user_prod, user_cant, productos)

if resultado:
    # Desempaquetamos la tupla
    stock_actual, alerta = resultado
    print(f"\n--- Movimiento de Almacén ---")
    print(f"Nuevo stock de {user_prod}: {stock_actual}")
    
    # Usamos un if simple para el mensaje de reabastecimiento
    mensaje = "SÍ" if alerta else "NO"
    print(f"¿Necesita reabastecer?: {mensaje}")
else:
    print("Error: El producto no existe en el inventario.")
    
    
"""
Variables que "guardan" estados: Fíjate cómo usamos alerta = nuevo_stock < 3. Esa variable guarda 
un True o un False directamente. Es mucho más limpio que hacer un if/else solo para retornar.

El poder de la Tupla: Cuando una función devuelve (a, b), puedes recibirlo en una sola variable 
(como hice con resultado) o en dos: stock, status = actualizar_y_revisar(...).

Nota mental: Los diccionarios son para buscar, las listas para ordenar y las funciones para procesar. 
No obligues a una a hacer el trabajo de la otra.
"""