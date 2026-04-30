# Corrección Problema 7: Usamos un flag (bandera)
intentos = 3
acceso = False

while intentos > 0:
    pin = input("PIN: ") # Mejor como string, los PIN pueden empezar con 0
    if pin == "1234":
        acceso = True
        break
    intentos -= 1
    print(f"Error. Te quedan {intentos}")

if acceso:
    print("Acceso concedido")
else:
    print("Tarjeta bloqueada")