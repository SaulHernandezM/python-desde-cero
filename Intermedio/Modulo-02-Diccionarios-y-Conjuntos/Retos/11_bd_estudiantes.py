"""
Reto: La Base de Datos de Estudiantes (Anidación Profunda)
Este reto simula un sistema escolar real.
    Crea un diccionario estudiantes donde cada llave es el ID del alumno (ej: "A1").
    El valor debe ser otro diccionario con: nombre y materias (donde materias es otro diccionario 
    con el nombre de la materia y la nota).
        {"A1": {"nombre": "Luis", "materias": {"Matematicas": 90, "Programacion": 100}}}
Misión:
    Pide al usuario el ID del alumno.
    Si existe, muestra su nombre y recorre sus materias para imprimir cada una con su nota.
    Cálculo Extra: Muestra el promedio de sus notas.
"""

estudiantes = {"A1": {"nombre": "Luis", "materias": {"Matematicas": 90, "Programacion": 100}}, 
               "A2": {"nombre": "Saul", "materias": {"Matematicas": 80, "Programacion": 100}},
               "A3": {"nombre": "Samuel", "materias": {"Matematicas": 75, "Programacion": 80}},
               "A4": {"nombre": "Said", "materias": {"Matematicas": 70, "Programacion": 70}}}

id_alumno = input("Ingresa un ID (A1, A2, A3, A4): ")
encontrado = False

if id_alumno in estudiantes:
    print(f"Estudiante: {estudiantes[id_alumno]}")
    for materia, nota in estudiantes.items():
        print("")
    
        
        
    



