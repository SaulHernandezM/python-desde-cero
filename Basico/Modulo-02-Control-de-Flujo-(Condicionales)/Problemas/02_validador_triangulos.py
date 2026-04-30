"""
Problema: El Validador de Triángulos
Pide al usuario tres longitudes (lado A, B y C).
    Objetivo: 1.  Primero, verifica si esos tres lados pueden formar un triángulo 
    (La suma de dos lados siempre debe ser mayor al tercero).
    2.  Si es válido, clasifícalo en: Equilátero (3 lados iguales), Isósceles (2 iguales) o Escaleno (todos distintos).
    3.  Si no es válido, muestra un error.
"""

print("### Validador de Triangulos ###")

# Variables en donde se guardan las longitudes de los lados del triangulo
lado_a = float(input("Ingresa la longitud del lado A: "))
lado_b = float(input("Ingresa la longitud del lado B: "))
lado_c = float(input("Ingresa la longitud del lado C: "))

# Verificacion si se puede formar un triangulo
triangulo = (lado_a + lado_b > lado_c) and (lado_b + lado_c > lado_a) and (lado_a + lado_c > lado_b)

if triangulo:
    print("La figura es un triangulo")

else:
    print("La figura no es un triangulo")
    
    
print("\n")
print("Que tipo de triangulo es la figura?")

# Comprobar el tipo de triangulo
if lado_a == lado_b == lado_c:
    print("Es un triangulo Equilátero (3 lados iguales)")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print("Es un triangulo Isósceles (2 iguales)")
elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
    print("Es un triangulo Escaleno (todos distintos)")
else:
    print("La figura no es un triangulo")

