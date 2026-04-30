"""
Problema: El Menú de Precios
Este ejercicio te ayudará a practicar el acceso y la actualización de datos.
    Crea un diccionario llamado menu con 3 productos y sus precios 
    (ej: {"pizza": 10, "soda": 2, "pasta": 8}).
    Lógica:
        Muestra el menú al usuario.
        Pide al usuario el nombre de un producto para ver su precio.
        Actualización: El restaurante subió los precios. Cambia el precio de uno de los productos 
        (ej: la pizza ahora cuesta 12).
        Agrega un nuevo producto llamado "postre" con un precio de 5.
    Imprime el menú final.
"""

menu = {"pizza": 10, "soda": 2, "pasta": 8}

print(f"Menu: {menu.keys()}")

producto = input("Ver precio del producto: ")
print(f"Precio: {menu[producto]}.")

menu["pizza"] = 12
menu["pastel"] = 5

print(f"Menu: {menu.keys()}")


# Gemini nota
"""
Si el usuario escribe "hamburguesa", tu línea menu[producto] provocará un error llamado KeyError 
y el programa se detendrá bruscamente.
Lección: Siempre que accedas a un diccionario usando una variable externa, usa un if producto in menu: 
(como hiciste muy bien en el Problema 2) o el método .get().
"""



