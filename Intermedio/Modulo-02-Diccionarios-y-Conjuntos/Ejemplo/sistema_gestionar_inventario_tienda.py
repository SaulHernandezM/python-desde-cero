# Creación de un diccionario: Llave es el producto, Valor es el precio
inventario = {
    "manzana": 1.5,
    "pan": 0.8,
    "leche": 1.2
}

# Acceso directo por llave
print(f"El precio del pan es: {inventario['pan']}")

# Agregar o actualizar
inventario["huevo"] = 2.5 

# Recorrer un diccionario (Súper útil)
for producto, precio in inventario.items():
    print(f"Articulo: {producto} | Precio: ${precio}")