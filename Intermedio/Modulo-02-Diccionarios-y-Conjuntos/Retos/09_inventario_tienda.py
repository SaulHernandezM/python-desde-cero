"""
Reto: El Mini-Inventario de Tienda (Diccionarios Anidados)
Este reto simula un sistema de ventas un poco más complejo.
    Crea un diccionario llamado tienda donde cada llave es un producto y el valor es otro diccionario con
    precio y categoria.
    tienda = {"Pan": {"precio": 1.0, "categoria": "Panadería"}, "Agua": {"precio": 0.5, 
    "categoria": "Bebidas"}}
    Misión:
        Pide al usuario que ingrese una Categoría (ej: "Bebidas").
        Recorre la tienda con un bucle for y muestra solo los productos que pertenezcan a esa categoría.
        Extra: Si no hay productos en esa categoría, avisa al usuario.
"""

tienda = {"Pan": {"precio": 10.5, "categoria": "Panaderia"}, 
          "Agua": {"precio": 15., "categoria": "Bebidas"},
          "Leche": {"precio": 27., "categoria": "Lacteos"},
          "Carne": {"precio": 120., "categoria": "Carniceria"}
        }

categoria = input("Categoria (Panaderia, Bebidas, Lacteos, Carniceria): ").strip()

if categoria in tienda:
    for producto, info in tienda.items():
        print(f"Producto: {producto}.")
        print(f"Informacion: {info}.")
else:
    print("Producto no encontrado.")



"""
Tu código hace if categoria in tienda:.
El error: Esto busca si la palabra "Bebidas" es una llave principal (como "Pan" o "Agua"). Como no lo es, 
se va al else.
La lógica correcta: Debes entrar a la tienda con un for, y una vez dentro de cada producto, 
preguntar por su categoría interna.
"""
