hotel = {
    "Piso1": ["Libre", "Ocupada", "Libre"], 
    "Piso2": ["Ocupada", "Ocupada", "Libre"],
    "Piso3": ["Ocupada", "Libre", "Libre"]
}

piso = input("Piso (Piso1, Piso2, Piso3): ").strip()
num_hab = int(input("Número de habitación (1, 2, 3): ")) - 1

# 1. Verificamos que el piso exista
if piso in hotel:
    # 2. Accedemos al valor en la lista usando el índice numérico
    estado_actual = hotel[piso][num_hab]
    
    if estado_actual == "Libre":
        hotel[piso][num_hab] = "Ocupada" # Actualizamos el valor en la lista
        print(f"¡Reserva exitosa en {piso}, habitación {num_hab + 1}!")
    else:
        print("Lo sentimos, esa habitación ya está ocupada.")
else:
    print("El piso ingresado no existe.")