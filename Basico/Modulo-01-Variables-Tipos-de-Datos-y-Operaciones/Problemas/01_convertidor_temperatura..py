"""
Problema: Convertidor de Temperatura.
Crea un programa que pida al usuario una temperatura en grados Celsius y la convierta a Fahrenheit.
Lo que se espera: El programa debe solicitar un número, realizar la operación matemática y mostrar el resultado con un mensaje claro.
Nota: Recuerda que input() siempre devuelve un texto (str), por lo que deberás convertirlo a un número usando float().
"""
print("### Convertidor de temperatura de grados Celsius a Fahrenheit ###")
grados_celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Formula para calcular Celsius a Fehrenheit
grados_fahrenheit = (grados_celsius * 9/5) + 32

print(f"Los grados Celsius ingresados son: {grados_celsius}")
print(f"La conversion de grados Celsius a grados Fahrenheit es: {grados_fahrenheit}")



