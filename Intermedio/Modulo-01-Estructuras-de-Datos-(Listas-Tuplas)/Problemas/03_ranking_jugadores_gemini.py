puntajes = []

for x in range(6):
    # Convertimos la entrada a entero para poder comparar valores numéricos
    nuevo_puntaje = int(input(f"Ingresa puntaje {x + 1}: "))
    puntajes.append(nuevo_puntaje)

# sorted() devuelve una nueva lista ordenada, no modifica la original (a menos que quieras)
puntajes_ordenados = sorted(puntajes, reverse=True)     
    
print(f"\nTop 3 de los mejores puntajes: {puntajes_ordenados[0:3]}")
print(f"Puntaje mas bajo: {puntajes_ordenados[-1]}")