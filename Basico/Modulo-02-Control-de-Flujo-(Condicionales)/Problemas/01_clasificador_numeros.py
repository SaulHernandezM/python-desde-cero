"""
Problema: El Clasificador de Números.
Crea un programa que pida al usuario un número entero.
    Lo que se espera: 1. Si el número es mayor a 0, imprimir "Es positivo".
    2. Si el número es menor a 0, imprimir "Es negativo".
    3. Si el número es exactamente 0, imprimir "Es cero".
    4. Extra: Indica también si el número es par o impar (Investiga el operador módulo %).
"""

print("### Clasificador de numeros ###")

# Variable donde se almacena el numero que se pide al usuario
numero = int(input("Ingresa un numero: "))

# Logica que evalua si un numero es par o impar
if numero > 0 and numero % 2 == 0:
    print("El numero es positivo y es par")
elif numero > 0 and numero % 2 == 1:
    print("El numero es positivo y es impar")
elif numero < 0 and numero % 2 == 0:
    print("El numero es negativo y es par")
elif numero < 0 and numero % 2 == 1:
    print("El numero es negativo y es impar")
else:
    print("El numero es cero")

