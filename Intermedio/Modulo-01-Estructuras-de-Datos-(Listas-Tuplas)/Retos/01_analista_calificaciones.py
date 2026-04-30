"""
El Analista de Calificaciones Pro.
Crea un programa que permita al usuario ingresar 5 calificaciones y las guarde en una lista.
    Una vez llena la lista, el programa debe calcular:
        El promedio exacto.
        La calificación más alta y la más baja (Investiga las funciones estándar max() y min()).
    Condición especial: El programa debe generar una nueva lista llamada aprobados que contenga 
    solo las notas de la lista original que sean mayores o iguales a 70.
"""

calificaciones_real = []
aprobados = []

for x in range(5):
    
    calificaciones = int(input(f"Ingrese calificacion {x + 1}: "))
    calificaciones_real.append(calificaciones)
    
    if calificaciones >= 70:
        aprobados.append(calificaciones)
        
    
promedio = sum(calificaciones_real) / len(calificaciones_real)
    
print(f"Promedio: {promedio}")
print(f"Calificacion mas alta: {max(calificaciones_real)}")
print(f"Calificacion mas baja: {min(calificaciones_real)}")
print(f"Calificaciones aprobatorias: {aprobados}")






