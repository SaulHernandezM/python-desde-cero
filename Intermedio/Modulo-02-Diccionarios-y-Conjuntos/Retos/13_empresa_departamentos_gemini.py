empresa = {"Ventas": [{"nombre": "Pablo", "puesto": "Marketing"}, {"nombre": "Karen", "puesto": "Analista Ventas"}],
           "IT": [{"nombre": "Ana", "puesto": "Dev"}, {"nombre": "Luis", "puesto": "Soporte"}]}


nombre_depa = input("Departamento (Ventas, IT): ").strip()

if nombre_depa in empresa:
    print(f"\n--- Personal de {nombre_depa} ---")
    # Recorremos la LISTA que está dentro de la llave del departamento
    for empleado_info in empresa[nombre_depa]:
        # 'empleado_info' es un diccionario individual
        nombre = empleado_info["nombre"]
        puesto = empleado_info["puesto"]
        print(f"Empleado: {nombre} | Cargo: {puesto}")
    
    total = len(empresa[nombre_depa])
    print(f"Total de personas en el departamento: {total}")
else:
    print("Departamento no encontrado.")