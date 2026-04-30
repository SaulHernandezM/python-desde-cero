estudiantes = {"A1": {"nombre": "Luis", "materias": {"Matematicas": 90, "Programacion": 100}}, 
               "A2": {"nombre": "Saul", "materias": {"Matematicas": 80, "Programacion": 100}},
               "A3": {"nombre": "Samuel", "materias": {"Matematicas": 75, "Programacion": 80}},
               "A4": {"nombre": "Said", "materias": {"Matematicas": 70, "Programacion": 70}}}

id_alumno = input("Ingresa un ID (A1, A2, A3, A4): ").strip()

if id_alumno in estudiantes:
    alumno = estudiantes[id_alumno] # Extraemos la "capa 1" (nombre y materias)
    print(f"\nEstudiante: {alumno['nombre']}")
    
    materias_dict = alumno["materias"] # Extraemos la "capa 2" (el dict de notas)
    suma_notas = 0
    
    print("Notas registradas:")
    for materia, nota in materias_dict.items():
        print(f"- {materia}: {nota}")
        suma_notas += nota
    
    # Cálculo del promedio
    promedio = suma_notas / len(materias_dict)
    print(f"\nPromedio General: {promedio:.2f}")
else:
    print("ID no encontrado.")