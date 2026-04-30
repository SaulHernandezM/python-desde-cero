"""
Problema: Formateador de Nombres Profesionales
Un usuario ingresa su nombre y apellido por separado, pero a veces escribe en minúsculas, otras en MAYÚSCULAS o mezclado.
Objetivo: Solicitar nombre y apellido, y mostrar un saludo formal donde la primera letra de cada palabra sea mayúscula y 
el resto minúscula (ejemplo: "Hola, Juan Perez").
Pista: Investiga el método de cadena .capitalize() o .title() en la biblioteca estándar de Python.
"""

print("### Formateador de Nombres Profesionales ###")

nombre = input("Ingrese su nombre: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
apellido_materno = input("Ingrese su apellido materno: ")

print(f"Hola, {nombre.capitalize()} {apellido_paterno.capitalize()} {apellido_materno.capitalize()}")