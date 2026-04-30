precio_sum = 0
precio_max = 0
precio_min = 0
dia_max = 0
dia_min = 0

for dia in range(1, 8):
    precio = float(input(f"Precio día {dia}: "))
    precio_sum += precio
    
    # Si es el primer día, este precio es tanto el máximo como el mínimo
    if dia == 1:
        precio_max = precio_min = precio
        dia_max = dia_min = dia
    else:
        # Comparaciones independientes
        if precio > precio_max:
            precio_max = precio
            dia_max = dia
        if precio < precio_min:
            precio_min = precio
            dia_min = dia

print(f"Promedio: {precio_sum / 7:.2f}")
print(f"Mínimo: {precio_min} (Día {dia_min})")
print(f"Máximo: {precio_max} (Día {dia_max})")