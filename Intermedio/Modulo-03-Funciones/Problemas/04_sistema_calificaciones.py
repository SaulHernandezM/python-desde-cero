"""
Problema: El Sistema de Calificaciones
Aquí vamos a ver cómo una función puede procesar toda una colección de datos.
Crea una función llamada calcular_promedio(notas) que reciba una lista de números y retorne el promedio.
Crea otra función llamada obtener_mencion(promedio) que retorne:
    "Excelente" si es ≥90.
    "Aprobado" si es ≥70.
    "Reprobado" si es menor a 70.
Misión: Pide al usuario 3 notas, guárdalas en una lista, pásala a la primera función y usa ese 
resultado para obtener la mención final.
"""

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def obtener_mencion(promedio):
    if promedio >= 90:
        return "Excelente"
    elif promedio >= 70:
        return "Aprobado"
    else:
        return "Reprobado"
    

print("#### Sistema Calificaciones ####")
calificaciones = []

for x in range(1, 4):
    user_notas = int(input(f"Nota {x}: "))
    # calificaciones.append(user_notas) <-- AHORA SÍ está dentro del bucle
    
calificaciones.append(user_notas)

promedio_alumno = calcular_promedio(calificaciones)
mencion = obtener_mencion(promedio_alumno)

print(f"Promedio alumno: {promedio_alumno}.")
print(f"Mencion: {mencion}.")



"""
En tu bucle for, cometiste un error de indentación:
Lo que pasó: Pusiste el calificaciones.append(user_notas) fuera del bucle. Por lo tanto, el programa 
pide 3 notas, pero solo guarda la última.
La consecuencia: Al hacer sum(notas) / len(notas), la lista solo tiene un elemento, así que el promedio 
siempre será igual a la última nota.
"""