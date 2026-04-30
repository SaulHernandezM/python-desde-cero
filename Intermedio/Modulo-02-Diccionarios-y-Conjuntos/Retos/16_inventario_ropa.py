"""
Reto: El Inventario de Ropa (Diccionario -> Diccionario -> Lista)
Este tiene una capa extra. Es una tienda que vende ropa por tallas.
    Crea un diccionario tienda. Las llaves son productos ("Camisa", "Pantalon"). El valor es otro 
    diccionario donde las llaves son "Tallas" y el valor es una lista de colores disponibles.
        {"Camisa": {"Tallas": ["S", "M", "L"], "Colores": ["Rojo", "Azul"]}}
    Misión:
        Pide al usuario el nombre del producto.
        Si existe, muestra todas las Tallas disponibles (recorriendo la lista).
        Luego, muestra todos los Colores disponibles.
        Extra: Pide al usuario un color. Si el color está en la lista de colores, dile "¡Lo tenemos!"
"""

tienda =  {"Camisa": {"Tallas": ["S", "M", "L", "XL"], "Colores": ["Rojo", "Azul", "Rosa", "Gris"]},
           "Pantalon": {"Tallas": ["S", "M", "L"], "Colores": ["Negro", "Blanco", "Azul"]}}

nombre_producto = input("Nombre Producto (Camisa, Pantalon): ")


if nombre_producto in tienda:
    for talla, color in tienda[nombre_producto].items():
        print(f"{talla}: {color}")

    color_user = input("Color: ")
    if color_user in tienda[nombre_producto]:
        print("¡Lo tenemos!")
    else:
        print("No lo tenemos.")
    
else:
    print("Producto no disponible.")


"""
Pequeño error en:
if color_user in tienda[nombre_producto]:.
¿Por qué falló?: tienda[nombre_producto] es el diccionario que tiene las llaves "Tallas" y "Colores".
Al usar in, Python busca en las llaves. Si el usuario escribe "Rojo", Python dice: "¿Es 'Rojo' igual a 'Tallas' o 'Colores'?".
La respuesta es False.
La solución: Debes apuntar directamente a la lista de colores:
if color_user in tienda[nombre_producto]["Colores"]:
"""
