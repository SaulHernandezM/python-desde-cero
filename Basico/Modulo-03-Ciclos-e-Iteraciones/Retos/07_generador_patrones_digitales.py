"""
Reto: El Generador de Patrones Digitales (Uso de for)
En programación, a veces necesitamos generar estructuras visuales o limpiar datos.
    Pide al usuario un número entero (ej: 5).
    Usa un bucle for para imprimir una escalera de asteriscos.
    Resultado esperado (si el usuario pone 5):
        *
        **
        ***
        ****
        *****
Pista: En Python puedes multiplicar un texto por un número: print("*" * 3) imprime ***.
"""

numero = int(input("Ingresa un numero: "))

for x in range(1, numero + 1):
    print("*" * x)


