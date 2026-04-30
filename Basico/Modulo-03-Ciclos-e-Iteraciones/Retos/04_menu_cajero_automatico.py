"""
Reto: El Menú de Cajero Automático
Simula la interfaz de un cajero.
    Inicia una variable saldo = 1000.
    Muestra un menú infinito que diga:
            Ver saldo
            Depositar dinero
            Retirar dinero
            Salir       
Lógica:
    Si elige 2, pide la cantidad y súmala al saldo.
    Si elige 3, pide la cantidad. OJO: No puedes retirar más de lo que tienes. Si intenta retirar más, muestra "Fondos insuficientes".
    El programa solo termina cuando elija la opción 4.
"""

saldo = 1000.

while True:
    
    print("\n#### Menu ####\n")
    print("1. Ver saldo.")
    print("2. Depositar dinero.")
    print("3. Retirar dinero.")
    print("4. Salir.")
    numero = int(input("Elija una opcion ingresando un numero: "))
    
    if numero == 1:
        print(f"Su saldo es de {saldo}.")
    
    elif numero == 2:
        deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print(f"Su nuevo saldo es de {saldo}")
    
    elif numero == 3:
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Usted retiro {retiro}.")
            print(f"Su nuevo saldo es de {saldo}.")
    
    elif numero == 4:
        print("Gracias por visitarnos.")
        break
        







