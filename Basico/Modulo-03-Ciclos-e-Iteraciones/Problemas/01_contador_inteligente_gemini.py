inicio = int(input("Inicio: "))
fin = int(input("Fin: "))

for num in range(inicio, fin + 1):
    if num % 3 == 0: # ¿Es el residuo de la división entre 3 igual a 0?
        print(f"{num} es múltiplo de 3")