"""
Reto: Calculadora de Promedios Académicos (Anidación Profunda)
    Crea un diccionario escuela donde cada llave es el nombre de un alumno y el valor es una lista 
    de diccionarios con sus materias y notas.
        {"Ana": [{"materia": "Mate", "nota": 90}, {"materia": "Prog", "nota": 100}]}
    Crea una función llamada generar_boletas(dicc_escuela).
    Misión: La función debe devolver un nuevo diccionario donde la llave sea el nombre del alumno y 
    el valor sea su promedio final.
"""

def generar_boletas(dicc_escuela):
    escuela_promedio = {}
    
    for alumno, info in dicc_escuela.items():
        for materias, notas in info:
            promedio = sum(notas) / len(materias)
            
            escuela_promedio[alumno] = promedio
            
    return escuela_promedio
    
    
escuela =  {"Ana": [{"materia": "Mate", "nota": 90}, {"materia": "Prog", "nota": 100}],
            "Saul": [{"materia": "Mate", "nota": 80}, {"materia": "Prog", "nota": 100}],
            "Pedro": [{"materia": "Mate", "nota": 80}, {"materia": "Prog", "nota": 90}],
            "Maria": [{"materia": "Mate", "nota": 70}, {"materia": "Prog", "nota": 70}]}


print(generar_boletas(escuela))



"""
Notas
Error de desempaquetado: En for materias, notas in info:, intentaste desglosar un diccionario como 
si fuera una tupla. info es una lista de diccionarios.

La solución: Debes iterar sobre la lista, extraer el valor de la llave "nota" de cada diccionario, 
sumarlos y luego dividir.
"""
