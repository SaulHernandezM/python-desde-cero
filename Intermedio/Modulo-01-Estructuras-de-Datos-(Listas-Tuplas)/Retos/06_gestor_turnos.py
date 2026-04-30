"""
Reto: El Gestor de Turnos (Listas)
Este reto simula la sala de espera de una clínica.
    Crea una lista vacía llamada fila_espera.
    Crea un menú que permita:
        1. Registrar paciente: Pide el nombre y agrégalo al final.
        2. Atender paciente: Elimina al primero de la fila y muestra su nombre. 
        Si no hay nadie, avisa: "No hay pacientes".
        3. Urgencia: Pide el nombre de un paciente y ponlo al principio de la fila (índice 0).
        4. Ver estado: Muestra cuántos faltan por atender y quién es el siguiente.
"""


fila_espera = []

while True:
    print("#### MENU ####")
    print("1. Registrar paciente.")
    print("2. Atender paciente.")
    print("3. Urgencia.")
    print("4. Ver estado.")
    print("5. Ver sala de espera.")
    print("6. Salir")
    opcion = int(input("Elige una opcion: "))
    
    # Registrar paciente
    if opcion == 1:
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        fila_espera.append(nombre_paciente)   
    # Atender paciente (gemini)    
    elif opcion == 2:
        if len(fila_espera) > 0: # 1. Verificamos si hay alguien
            paciente_actual = fila_espera.pop(0) # 2. Sacamos y GUARDAMOS el nombre
            print(f"Atendiendo ahora a: {paciente_actual}")
        else:
            print("No hay pacientes en espera.")    
    # Atender paciente (no funciona)
    #elif opcion == 2:
    #    if fila_espera.pop(0):
    #        print(f"Adelante {fila_espera[0]}.")
    #   else:
    #      print("No hay pacientes.")
    # Urgencia
    elif opcion == 3:
        nombre_paciente = input("Ingrese el nombre del paciente: ")
        fila_espera.insert(0, nombre_paciente)
    # Ver estado
    elif opcion == 4:
        print(f"Quedan {len(fila_espera)} pacientes por atender.")
        print(f"El siguiente en pasar es: {fila_espera[0]}")
    # Ver lista
    elif opcion == 5:
        print(fila_espera)
    # Salir
    else:
        print("Adios.")
        break