def agrupar_por_categoria(lista_productos):
    resultado = {}
    
    for p in lista_productos:
        cat = p["categoria"]
        nombre = p["nombre"]
        
        # 1. Si la categoría NO existe aún en nuestro resultado,
        # la creamos con una lista vacía.
        if cat not in resultado:
            resultado[cat] = []
            
        # 2. Ahora que estamos seguros de que existe la lista,
        # simplemente añadimos el nombre.
        resultado[cat].append(nombre)
        
    return resultado

productos = [{"nombre": "Teclado", "precio": 25, "categoria": "IT"}, 
             {"nombre": "Monitor", "precio": 200, "categoria": "IT"}, 
             {"nombre": "Silla", "precio": 150, "categoria": "Muebles"},
             {"nombre": "Mesa", "precio": 250, "categoria": "Muebles"},
             {"nombre": "Mouse", "precio": 10, "categoria": "IT"}]

nuevo_dicc = agrupar_por_categoria(productos)

print(nuevo_dicc)

# Al ejecutar, obtendrás: {'IT': ['Teclado', 'Monitor', 'Mouse'], 'Muebles': ['Silla', 'Mesa']}