while True:
    try:
        calificacion = int(input("Ingrese una calificación (0-10): "))
        
        # Usamos 'and' para asegurar que esté en el rango exacto
        if calificacion >= 0 and calificacion <= 10:
            print(f"Registro exitoso: {calificacion}")
            break
        else:
            print("Error: La nota debe estar entre 0 y 10.")
    except ValueError:
        print("Error: Solo se permiten números enteros.")