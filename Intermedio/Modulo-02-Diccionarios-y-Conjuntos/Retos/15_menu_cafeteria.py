"""
Reto: El Menú de Cafetería (Cálculos Anidados)
Aquí vamos a mezclar diccionarios y listas para generar una "cuenta".
    Crea un diccionario menu. Las llaves son categorías ("Cafe", "Postre"). Cada valor es una 
    lista de diccionarios con item y precio.
        {"Cafe": [{"item": "Espresso", "precio": 2.5}, {"item": "Latte", "precio": 3.5}]}
    Misión:
        Muestra todas las categorías disponibles.
        El usuario elige una categoría.
        El programa debe mostrar todos los items de esa categoría y calcular el precio promedio de 
        los productos de esa sección.
"""

menu = {"Cafe": [{"item": "Espresso", "precio": 2.5}, {"item": "Latte", "precio": 3.5}],
        "Postre": [{"item": "Pastel de chocolate", "precio": 10.5}, {"item": "Pay limon", "precio": 5.5}]}

print(f"Categorias: {menu.keys()}")
suma_precio = 0
elegir_categoria = input("Escoge categoria: ") 

if elegir_categoria in menu:
    for articulo, costo in menu[elegir_categoria]:
        print(f"Menu de {elegir_categoria}: {menu[elegir_categoria][articulo]}.")
else:
    print("Categoria no encontrada.")
    
    
    
    
"""
for variable1, variable2 in lista_de_diccionarios:.
El error: Python solo puede "desempaquetar" así si la lista contiene tuplas de dos elementos 
(como vimos en el reto de los vuelos).
La realidad: Tu lista contiene Diccionarios. Por lo tanto, el bucle for solo puede tomar un objeto
a la vez (el diccionario completo).
"""
