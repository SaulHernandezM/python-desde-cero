"""
Problema: El Cajero con Intentos (while + contador)
Objetivo: Gestionar un sistema con un límite de oportunidades.
    Descripción: Un usuario intenta ingresar su PIN secreto.
    Instrucciones: El PIN correcto es "1234". El usuario tiene 3 intentos. 
    Si falla, resta 1 a sus intentos. Si llega a 0, el programa dice "Tarjeta bloqueada". 
    Si acierta antes, dice "Acceso concedido" y el bucle debe terminar.
    Pista: Usa un while intentos > 0:.
"""

intentos = 3

while intentos > 0:
    pin = int(input("Ingresa tu PIN: "))
    
    if pin != 1234:
        intentos -= 1
        print(f"PIN incorrecto. Te quedan {intentos} intentos.")
        if intentos == 0:
            print("Tarjeta bloqueada.")
            break
    else:
        print("Acceso concedido.")
        break

