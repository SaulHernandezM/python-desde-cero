"""
Reto: El Sistema de Inscripciones (Diccionario de Conjuntos)
Imagina que gestionas una escuela. Tienes una lista de alumnos y el curso al que se inscribieron.
    Crea una lista de tuplas: inscripciones = [("Luis", "Python"), ("Ana", "Java"), ("Luis", "Diseño")].
    Crea una función organizar_cursos(lista).
    Misión: Retornar un diccionario donde las llaves sean los cursos y los valores sean 
    Conjuntos (Sets) con los nombres de los alumnos.
        ¿Por qué sets? Porque si un alumno se inscribe dos veces al mismo curso por error, 
        el set lo limpiará automáticamente.
        Resultado esperado: {"Python": {"Luis"}, "Java": {"Ana"}, "Diseño": {"Luis"}}.
"""

def organizar_cursos(lista_inscripciones):
    cursos = {}
    for alumno, curso in lista_inscripciones:
        # Si el curso no está en el diccionario, creamos un set vacío para él
        if curso not in cursos:
            cursos[curso] = set()
        
        # Agregamos al alumno al set (el set evita duplicados automáticamente)
        cursos[curso].add(alumno)
    return cursos

inscripciones = [("Luis", "Python"), ("Ana", "Java"), ("Luis", "Diseño"), ("Pepe", "Java"), 
                 ("Carmen", "Diseño"), ("Sofia", "Python"), ("Pedro", "Python")]


cursos_organizados = organizar_cursos(inscripciones)

print(cursos_organizados)