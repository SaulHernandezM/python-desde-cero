"""
Reto: El Gestor Escolar (Diccionario de Listas)
En el mundo real, los valores de un diccionario no siempre son un simple número; a veces son 
estructuras completas.
    Crea un diccionario llamado alumnos donde la llave sea el nombre del estudiante y 
    el valor sea una lista de sus calificaciones.
    Ejemplo: {"Luis": [80, 90, 100], "Ana": [95, 85, 90]}
    Misión:
        Pide al usuario el nombre de un alumno.
        Si existe, pide una nueva calificación y agrégala a su lista (usa .append()).
        Calcula y muestra su promedio final usando la fórmula:
        promedio = sumatoria (calificaciones) / total elementos
        Si no existe, dile que el alumno no está registrado.
"""

alumnos = {"Luis": [80, 90, 100], "Ana": [95, 85, 90], "Flor": [100, 80, 90], "Pepe": [75, 95, 90], 
           "Carlos": [85, 95, 70], "Saul": [85, 85, 90], "Octavio": [75, 75, 70], "Pedro": [85, 75, 100], 
           "Maria": [75, 85, 80], "Javier": [75, 85, 80], "Julio": [100, 85, 70], "Juan": [85, 85, 80]}

nombre_alumno = input("Nombre del alumno: ")

if nombre_alumno in alumnos:
    nueva_calificacion = int(input("Nueva calificacion: "))
    alumnos[nombre_alumno].append(nueva_calificacion)
    
    lista_notas = alumnos[nombre_alumno]
    
    promedio = sum(lista_notas) / len(lista_notas)
    print(f"Calificaciones {nombre_alumno}: {lista_notas}.")
    print(f"Promedio final {promedio}.")
    
else:
    print("Alumno no registrado.")
    