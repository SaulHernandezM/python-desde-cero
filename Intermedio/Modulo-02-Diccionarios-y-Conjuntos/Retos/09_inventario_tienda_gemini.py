tienda = {
    "Pan": {"precio": 10.5, "categoria": "Panaderia"}, 
    "Agua": {"precio": 15.0, "categoria": "Bebidas"},
    "Leche": {"precio": 27.0, "categoria": "Lacteos"},
    "Carne": {"precio": 120.0, "categoria": "Carniceria"}
}

cat_buscada = input("Categoría a buscar: ").strip()
encontrado = False

# Primero recorremos todos los productos
for producto, info in tienda.items():
    # Buscamos la categoría DENTRO del diccionario 'info'
    if info["categoria"].lower() == cat_buscada.lower():
        print(f"-> {producto}: ${info['precio']}")
        encontrado = True

if not encontrado:
    print("No hay productos en esa categoría.")