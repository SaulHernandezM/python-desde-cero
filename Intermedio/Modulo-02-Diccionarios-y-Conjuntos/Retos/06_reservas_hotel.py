"""
Reto: Sistema de Reservas de Hotel (Diccionarios Anidados)
Imagina que gestionas un pequeño hotel de 3 pisos.
    Crea un diccionario llamado hotel. Las llaves son el número de piso ("Piso1", "Piso2") 
    y los valores son listas que indican si las habitaciones están "Ocupada" o "Libre".
    hotel = {"Piso1": ["Libre", "Ocupada", "Libre"], "Piso2": ["Ocupada", "Ocupada", "Libre"]}
    Misión:
        Pide al usuario el piso y el número de habitación (índice 0, 1 o 2).
        Si la habitación está "Libre", cámbiala a "Ocupada" y confirma la reserva.
        Si ya está "Ocupada", dile al usuario: "Lo sentimos, habitación no disponible".
"""

hotel = {"Piso1": ["Libre", "Ocupada", "Libre"], "Piso2": ["Ocupada", "Ocupada", "Libre"],
        "Piso3": ["Ocupada", "Libre", "Libre"]}

piso = input("Piso: ")
num_habitacion = int(input("Numero habitacion: ")) - 1

if hotel[piso][num_habitacion] == hotel[piso]["Libre"]:
    hotel[piso]["Libre"] = hotel[piso]["Ocupada"] 
    print(hotel[piso][num_habitacion])



