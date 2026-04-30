"""
Problema: El Contador Inteligente.
Pide al usuario un número de inicio y un número de fin.
    Lo que se espera: Usa un bucle for y range() para mostrar todos los números entre ese rango.
    Extra: Solo muestra los números que sean múltiplos de 3.
"""

num_user_inicio = int(input("Ingrese un numero de inicio: "))
num_user_final = int(input("Ingrese un numero de fin: "))

for x in range(num_user_inicio, num_user_final):
    if x // 3 == 0:
        print(x)
    