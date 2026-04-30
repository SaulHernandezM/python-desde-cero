"""
Reto: El "Número Secreto" (Uso de while)
Este reto simula un proceso de búsqueda binaria intuitiva.
    Define un número secreto (ej: numero_secreto = 42).
    El programa debe pedir al usuario que adivine el número.
    Lógica:
        Si el usuario falla, el programa debe decirle si el número 
        secreto es mayor o menor al que ingresó.
        El bucle debe repetirse hasta que el usuario acierte.
        Al final, debe decir en cuántos intentos lo logró.
"""

print("#### ADIVINA EL NUMERO SECRETO ####")

numero_secreto = 44
intentos = 0

while True:
    numero_usuario = int(input("Ingresa el numero secreto: "))
    intentos += 1
    if numero_secreto == numero_usuario:
        print("¡INCREIBLE! Adivinaste el numero secreto.")
        print(f"Intentos: {intentos}")
        break
    elif numero_secreto != numero_usuario:
        print("Fallaste. Intentalo de nuevo.")
    else:
        print("Solo se permiten numeros.")
    





