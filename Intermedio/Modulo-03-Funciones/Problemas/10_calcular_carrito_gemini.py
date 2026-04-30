def calcular_total(lista_compras, diccionario_precios):
    suma = 0
    for item in lista_compras:
        # Verificamos si el item de la lista existe en la tienda
        if item in diccionario_precios:
            suma += diccionario_precios[item] # Sumamos el valor asociado a esa llave
    return suma

precios = {"Huevo": 94., "Leche": 27., "Sabritas": 21., "Galletas": 20., "Gansito": 22., "Frijoles": 15.}

compras = []

print(precios)
num_productos = int(input("Productos a comprar (1-n): "))

for x in range(1, num_productos + 1):
    producto = input("Nombre producto: ")
    compras.append(producto)
   
total_compra = calcular_total(compras, precios)
print(f"Productos comprados: {compras}.")
print(f"Total de la compra: {total_compra}.")    