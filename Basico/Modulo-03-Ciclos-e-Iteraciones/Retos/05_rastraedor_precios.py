"""
Reto: El Rastreador de Precios (Buscador de Minímos/Máximos)
Imagina que estás analizando el precio del Bitcoin durante una semana.
    Pide al usuario que ingrese 7 precios (uno por cada día). Usa un bucle for.
    Al final de los 7 días, el programa debe decir:
        El precio promedio de la semana.
        El día que el precio estuvo más bajo.
        El día que el precio estuvo más alto.
        Pista: Usa una variable dia_max y dia_min para guardar en qué iteración (1 al 7) ocurrió el evento.
"""

dia_max = 0
dia_min = 1247287.21
dia = 0
guardar_dia_max = 0
guardar_dia_min = 0
precio_sum = 0

for x in range(1, 8):
    precio = float(input(f"Ingrese el precio del Bitcoin para el dia {x}: "))
    dia += 1
    precio_sum += precio
    
    if precio > dia_min:
        dia_max = precio
        guardar_dia_max = dia
    
    elif precio < dia_min:
        dia_min = precio
        guardar_dia_min = dia

print("\n")
print(f"El precio promedio del Bitcoin en la semana fue de {precio_sum / 7}.")
print(f"El dia {guardar_dia_min} el precio del Bitcoin fue el mas bajo: {dia_min}.")
print(f"El dia {guardar_dia_max} el precio del Bitcoin fue el mas alto: {dia_max}.")








