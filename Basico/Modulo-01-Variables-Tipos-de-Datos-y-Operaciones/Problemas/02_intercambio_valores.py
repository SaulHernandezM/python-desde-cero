"""
Problema: El Intercambiador de Valores
Este es un clásico de las entrevistas técnicas para principiantes.
Problema: Tienes dos variables, a = 5 y b = 10.
Objetivo: Intercambiar sus valores de modo que a valga 10 y b valga 5.
Restricción: Intenta hacerlo de dos formas:
    Usando una variable temporal (auxiliar).
    Usando la sintaxis especial de Python para asignación múltiple (revisa la documentación sobre Target lists).
"""

print("### Intercambio de valores ###")
print("### Metodo uno ###")
a = 5
b = 10

print("Valores originales")
print(f"a vale: {a}")
print(f"b vale: {b}")

print("\n")

temp = a
a = b
b = temp

print("Valores intercambiados")
print(f"a vale: {a}")
print(f"b vale: {b}")

print("\n")

print("### Metodo dos ###")

c = 4
d = 8

print("Valores originales")
print(f"c vale: {c}")
print(f"d vale: {d}")

print("\n")

c, d = d, c

print("Valores intercambiados")
print(f"c vale: {c}")
print(f"d vale: {d}")
