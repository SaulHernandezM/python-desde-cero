"""
Reto: La Meta de Ahorro (Uso de while)
Este reto simula una aplicación de finanzas personales.
    Pide al usuario una Meta de Ahorro (ejemplo: 500).
    Usa un bucle while para pedir "Depósitos" al usuario.
    Lógica:
        El bucle debe continuar mientras el ahorro total sea menor a la meta.
        En cada depósito, muestra cuánto falta para llegar a la meta.
    Final: Cuando alcance o supere la meta, felicita al usuario y dile cuánto 
    dinero extra (sobrante) le quedó.
"""

meta_ahorro = 0
deposito = 0
meta_lograda = 0

meta_ahorro = float(input("Ingrese la meta de ahorro: "))

while True: 
    deposito = float(input("Ingrese un deposito: "))
    meta_lograda += deposito
    
    if meta_lograda < meta_ahorro:
        print(f"Su deposito es de {deposito} te faltan {meta_ahorro - meta_lograda} para llegar a la meta de ahorro.\n")
    
    elif meta_lograda >= meta_ahorro:
        print(f"¡Felicidades! Acabas de llegar a la meta de ahorro de {meta_ahorro}.")
        print(f"Tienes un sobrante de {meta_lograda - meta_ahorro}.")
        break
    
    




