"""
Problema: El Lanzamiento de Cohete (while)
Objetivo: Practicar contadores que disminuyen (decremento).
    Descripción: Necesitamos una cuenta regresiva para un despegue.
    Instrucciones: Crea una variable contador que empiece en 10. Usa un bucle while para imprimir el valor 
    de contador mientras sea mayor a 0. Dentro del bucle, resta 1 a contador en cada paso.
    Resultado esperado: Una lista del 10 al 1 y, al final, el mensaje "¡IGNICIÓN!"
"""

contador = 10

while contador > 0:
    print(contador)
    contador -= 1
    
print("¡IGNICIÓN!")


