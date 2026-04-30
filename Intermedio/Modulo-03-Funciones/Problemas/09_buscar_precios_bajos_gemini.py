def buscar_baratos(productos, presupuesto):
    productos_presupuesto = []
    
    # Usamos .items() para tener el nombre y el precio a la mano
    for nombre, precio in productos.items():
        if precio <= presupuesto:
            productos_presupuesto.append(nombre)
            
    return productos_presupuesto # El return va FUERA del for

productos = {"Pan": 7.0, "Leche": 27.0, "Carne": 124.5, "Huevos": 94.5, "Cereal": 90.0, "Jugo": 24.0}
usuario_presupuesto = float(input("Presupuesto: "))

disponibles = buscar_baratos(productos, usuario_presupuesto)
print(f"Con ${usuario_presupuesto} puedes comprar: {disponibles}")