"""
Problema: El Mejor Promedio
Aquí mezclaremos diccionarios con listas como valores.
Crea un diccionario donde las llaves sean nombres de alumnos y los valores sean una lista de 3 notas.
estudiantes = {"Ana": [90, 80, 100], "Luis": [70, 60, 80]}
Crea una función llamada promedio_alumno(nombre, diccionario).
Misión: La función debe recibir el nombre de un alumno, buscar su lista de notas en el diccionario 
y retornar el promedio de esas notas.
Uso: Pide al usuario el nombre de un alumno y muestra su promedio.
"""

def promedio_alumno(nombre, diccionario):
    for nombre, nota in diccionario.items():
        if nombre in diccionario.keys():
            return nota
        else:
            return "Alumno no encontrado"

estudiantes = {"Ana": [90, 80, 100], "Luis": [70, 60, 80], "Pepe": [79, 80, 90]}


nombre_alumno = input("Alumno: ")
buscar_alumno = promedio_alumno(nombre_alumno, estudiantes)

print(f"Calificaciones de {nombre_alumno}: {buscar_alumno}.")


"""
Tu función devolvía siempre el primer alumno por dos razones:
Sombreado de variables: Usaste for nombre, nota in .... El nombre del bucle "tapó" al nombre que el 
usuario escribió.
El Return Impaciente: Como vimos antes, el return detiene la función. En la primera vuelta del bucle 
(donde está "Ana"), la función encuentra un return y se sale de inmediato.
La Regla de Oro: ¡Para buscar en un diccionario NO necesitas un bucle for! Esa es la magia de los 
diccionarios: pides la llave y él te da el valor al instante.
"""
