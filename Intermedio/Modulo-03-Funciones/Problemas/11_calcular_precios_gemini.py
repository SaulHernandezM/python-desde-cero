def aplicar_inflacion(diccionario_productos, porcentaje):
    for producto, costo in diccionario_productos.items():
        # Calculamos el aumento
        aumento = costo * (porcentaje / 100)
        diccionario_productos[producto] = costo + aumento
    return diccionario_productos

precios = {"Huevo": 94., "Leche": 27., "Sabritas": 21., "Galletas": 20., "Gansito": 22., "Frijoles": 15.}
# Aplicamos un 10% de inflación
tienda_cara = aplicar_inflacion(precios, 10)
print(f"Nuevos precios: {tienda_cara}")