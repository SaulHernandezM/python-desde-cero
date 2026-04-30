numero_secreto = 44
intentos = 0

while True:
    entrada = input("Adivina el número (o escribe 'salir'): ")
    
    if entrada.lower() == 'salir':
        break
        
    numero_usuario = int(entrada)
    intentos += 1
    
    if numero_usuario == numero_secreto:
        print(f"¡LOGRADO! Lo hiciste en {intentos} intentos.")
        break
    elif numero_usuario < numero_secreto:
        print("Pista: El número es MAYOR.")
    else:
        print("Pista: El número es MENOR.")