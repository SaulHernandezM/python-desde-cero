suma_num = 0
num_max = 0
procesados = 0

while True:
    n = int(input("Ingresa un número (negativo para salir): "))
    
    if n < 0:
        break # Salida inmediata
        
    # Si llegamos aquí, es 0 o positivo
    suma_num += n
    procesados += 1
    
    # Comprobamos el máximo de forma independiente
    if n > num_max:
        num_max = n

print(f"Suma: {suma_num} | Máximo: {num_max} | Total: {procesados}")