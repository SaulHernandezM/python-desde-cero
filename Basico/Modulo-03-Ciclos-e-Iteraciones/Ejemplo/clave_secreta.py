CLAVE_SECRETA = "python123"
intentos = 3

while intentos > 0:
    password = input(f"Introduce la clave (Intentos restantes {intentos}): ")
    
    if password == CLAVE_SECRETA:
        print("¡Acceso concedido!")
        break  # Salimos del bucle inmediatamente
    else:
        intentos -= 1  # Restamos 1 al contador
        print("Clave incorrecta.")

if intentos == 0:
    print("Cuenta bloqueada por seguridad.")