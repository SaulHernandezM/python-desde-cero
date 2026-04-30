calificaciones_real = []
aprobados = []

for x in range(5):
    # Este bucle se repite hasta que el usuario dé una nota válida
    while True:
        nota = int(input(f"Ingrese calificación {x + 1} (0-100): "))
        
        if 0 <= nota <= 100:
            calificaciones_real.append(nota)
            if nota >= 70:
                aprobados.append(nota)
            break  # Rompe el WHILE y pasa al siguiente ciclo del FOR
        else:
            print("ERROR: La nota debe estar entre 0 y 100.")

# Cálculos (usando tus excelentes funciones)
promedio = sum(calificaciones_real) / len(calificaciones_real)

print("-" * 30)
print(f"Promedio: {promedio:.2f}")
print(f"Calificación más alta: {max(calificaciones_real)}")
print(f"Calificación más baja: {min(calificaciones_real)}")
print(f"Aprobados: {aprobados}")