"""
Problema: El Generador de Tablas (Bucle anidado básico)
Objetivo: Entender que un bucle puede vivir dentro de otro.
    Descripción: Crear una tabla de multiplicar pequeña.
    Instrucciones: Pide un número al usuario (ej: 5). 
    Usa un for que vaya del 1 al 10 para imprimir la tabla de ese número.
    Formato esperado:
    5 x 1 = 5
    5 x 2 = 10
    ... (hasta el 10).
"""

numero = int(input("Ingresa la tabla a multiplicar: "))
multi = 0
resultado = 0

for x in range(1, 11):
    multi += 1
    resultado = numero * multi
    
    print(f"{numero} x {multi} = {resultado}")

"""
Está perfecto, pero recuerda que x ya es el número que necesitas. No hace falta crear multi.
"""