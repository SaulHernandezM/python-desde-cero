"""
Problema: El Sumador de Pares (for + if)
Objetivo: Filtrar información dentro de una repetición.
    Descripción: Queremos sumar únicamente los números pares en un rango.
    Instrucciones: Haz un bucle que recorra los números del 1 al 50. 
    Si el número es par, súmalo a una variable suma_pares.
    Resultado esperado: Al final, imprime el total de la suma de todos los pares entre 1 y 50.
"""

suma_pares = 0

for x in range(1, 51):
    if x % 2 == 0:
        suma_pares += x

print(f"La suma de todos los numeros pares del 1 al 50 es de {suma_pares}.")

