def analizar_usuarios(dicc_servicios):
    netflix = dicc_servicios["Netflix"]
    disney = dicc_servicios["Disney"]
    
    # Realizamos las operaciones directamente
    return {
        "ambos": netflix.intersection(disney),
        "solo_netflix": netflix.difference(disney),
        "total_unicos": len(netflix.union(disney)) # Unión para el total real
    }

servicios = {"Netflix": {"Saul", "Samuel", "Said", "Jose", "Manuel", "Maria"},
             "Disney": {"Saul", "Maria", "Samuel"}}

# Uso correcto: Guardar en variable primero
resultado = analizar_usuarios(servicios)
print(f"Ambos: {resultado['ambos']}")
print(f"Total únicos: {resultado['total_unicos']}")