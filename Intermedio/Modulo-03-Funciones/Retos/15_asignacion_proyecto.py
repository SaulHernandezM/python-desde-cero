"""
Reto: Asignación de Proyectos (Filtros de Sets y Listas)
Imagina una empresa de software.
    Crea un diccionario empleados donde cada llave es el nombre y el valor es un Set de sus 
    habilidades tecnológicas.
    Crea una lista llamada proyecto_requisitos que contenga las habilidades necesarias 
    (ej. ["Python", "SQL"]).
    Misión: Crea una función encontrar_candidatos(dicc_empleados, lista_requisitos).
    Lógica: Un empleado es candidato solo si su set de habilidades tiene todas las habilidades 
    de la lista de requisitos.
    Pista: Convierte la lista de requisitos a un set y usa el método .issubset() o el operador <=.
"""

def encontrar_candidatos(dicc_empleados, lista_requisitos):
    candidato_cumple = []
    candidato_nocumple = []
    
    for empleado, lenguajes in dicc_empleados.items():
        #   if lenguajes.issubset(lista_requisitos):
        if set(lista_requisitos).issubset(lenguajes):     
            candidato_cumple.append(empleado)
        else:
            candidato_nocumple.append(empleado)
    
    return candidato_cumple, candidato_nocumple
    
empleados = {"Saul": {"Python", "SQL", "R"}, "Samuel": {"C++", "C#", "Java"}, 
             "Said": {"Python"}, "Manuel": {"Python", "SQL"}, 
             "Maria": {"SQL", "R"}, "Luis": {"Prolog", "Haskell"},
             "Manolo": {"Python", "R"}, "Alexia": {"Python", "Java"}}

proyecto_requisito = ["Python", "SQL"]

cumplen, no_cumplen = encontrar_candidatos(empleados, proyecto_requisito)

print(f"Candidatos cumplen: {cumplen}")
print(f"Candidatos no cumplen: {no_cumplen}")


"""
Nota
if lenguajes.issubset(lista_requisitos):
Lógica del Negocio: En un entorno real, si un proyecto requiere ["Python", "SQL"] y un candidato sabe 
{"Python", "SQL", "R"}, él debería ser apto porque cumple con el mínimo solicitado.

El Comportamiento de tu Código: Con .issubset(), estás preguntando: ¿Son las habilidades del empleado 
un subconjunto de los requisitos?Si Saul sabe {"Python", "SQL", "R"}, tu código dice que NO cumple, 
porque "R" no está en los requisitos. Si Said sabe {"Python"}, tu código dice que SÍ cumple, porque 
"Python" es un subconjunto de los requisitos.

La Corrección Lógica: Lo que buscamos es que los requisitos sean un subconjunto de las habilidades 
del empleado. En Python: set(lista_requisitos).issubset(lenguajes) o usando el 
operador de superconjunto: lenguajes >= set(lista_requisitos).
"""

