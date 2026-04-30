"""
Reto: Sistema de Calificaciones de una Academia.
Debes construir un evaluador de notas final. El sistema pedirá una calificación del 0 al 100 
y debe mostrar un mensaje basado en la siguiente escala técnica:
    90 - 100: "Nivel: Experto (A)".
    80 - 89: "Nivel: Avanzado (B)".
    70 - 79: "Nivel: Competente (C)".
    60 - 69: "Nivel: Principiante (D)".
    Menos de 60: "Nivel: Insuficiente (F)".
Regla de Negocio Adicional: Si la nota ingresada es mayor a 100 o menor a 0, el programa debe mostrar 
un error de "Entrada inválida" y no procesar la calificación.
"""

print("### Sistema de Calificaciones de una Academia ###")

# Varible donde se guarda la calificacion
calificacion = int(input("Ingrese la calaficacion: "))

# Logica para evaluar si la calificacion es mayor a 100 o menor o igual a cero
if calificacion > 100 or calificacion <= 0:
    print("Entrada invalida")

# Logica para evaluar la nota final
elif calificacion >= 90:
    print("Nivel: Experto (A)")
elif calificacion >= 80:
    print("Nivel: Avanzado (B)")
elif calificacion >= 70:
    print("Nivel: Competente (C)")
elif calificacion >= 60:
    print("Nivel: Principiante (D)")
else:
    print("Nivel: Insuficiente (F)")
