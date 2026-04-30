"""
Reto: El Almacén Inteligente (Diccionarios Anidados)
En este reto, los valores de tu diccionario serán otro diccionario. Esto es lo que llamamos 
"objetos complejos".
    Crea un diccionario llamado productos. Cada llave será el nombre de un producto y el valor 
    será un diccionario con precio y stock.
        Ejemplo: {"Laptop": {"precio": 1200, "stock": 5}, "Mouse": {"precio": 25, "stock": 10}}
Misión:
    Pide al usuario el nombre de un producto.
    Si existe, muestra su precio y su stock actual.
    Pregunta: "¿Cuántas unidades se vendieron?".
    Lógica: Resta esa cantidad al stock. Si el stock llega a 0, imprime una alerta: "¡Producto agotado!".
    Si el usuario pide más de lo que hay en stock, dile: "Venta no posible, solo quedan [cantidad]".
Recuerda que para entrar al "segundo nivel" del diccionario usas doble corchete: productos["Laptop"]["stock"].
"""

productos = {"Laptop": {"precio": 1200, "stock": 5}, "Mouse": {"precio": 25, "stock": 10}, 
            "Teclado": {"precio": 50, "stock": 20}, "Audifonos": {"precio": 100, "stock": 30}, 
            "HDMI": {"precio": 10, "stock": 10}}

nombre_producto = input("Producto: ")

if nombre_producto in productos:
    print(productos[nombre_producto])
    
    unidades_vendidas = int(input("¿Cuántas unidades se vendieron?: "))
    resta_stock = productos[nombre_producto]["stock"]  - unidades_vendidas
    
    if unidades_vendidas > productos[nombre_producto]["stock"]:
        print(f"Venta no posible, solo quedan {productos[nombre_producto]["stock"]}.")
    elif resta_stock == 0:
        print("¡Producto agotado!")
    else:
        print(f"Stock: {resta_stock}")
    
else:
    print("Producto no encontrado.")



"""
El error de las comillas: En tu f-string escribiste: {productos[nombre_producto]["stock"]}. 
Al usar comillas dobles afuera y comillas dobles adentro, Python se confunde y piensa que el
texto termina antes de tiempo.

Regla de oro: Si usas comillas dobles " para el f-string, usa comillas simples ' para las llaves 
del diccionario adentro.

La actualización de datos: Al igual que en el reto anterior, calculas resta_stock, pero no actualizas 
el diccionario original. Si no haces productos[nombre_producto]["stock"] = resta_stock, el inventario 
nunca bajará realmente.
"""
