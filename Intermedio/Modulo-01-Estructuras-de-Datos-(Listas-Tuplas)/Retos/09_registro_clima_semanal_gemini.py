semana = [("Lunes", 22), ("Martes", 25), ("Miércoles", 19), 
          ("Jueves", 20), ("Viernes", 15), ("Sábado", 29), ("Domingo", 18)]

# Inicializamos con el primer día como referencia
dia_max, temp_max = semana[0]
dia_min, temp_min = semana[0]

for dia, temp in semana:
    if temp > temp_max:
        temp_max = temp
        dia_max = dia
    if temp < temp_min:
        temp_min = temp
        dia_min = dia

print(f"El día más caluroso fue {dia_max} con {temp_max}°C")
print(f"El día más frío fue {dia_min} con {temp_min}°C")