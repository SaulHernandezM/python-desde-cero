"""
Reto: El Analista de Números (El "Gran Acumulador")
Este reto simula un procesamiento de datos estadísticos simple.
    Misión: El programa debe pedir números al usuario uno por uno.
    Condición de salida: El proceso termina cuando el usuario ingresa un número negativo.
    Resultados esperados: Al final (cuando se ingrese el negativo), el programa debe mostrar:
        La suma total de todos los números positivos ingresados.
        Cuál fue el número más grande (máximo) ingresado.
        Cuántos números en total se procesaron (sin contar el negativo final).
"""

numeros_procesados = 0
suma_num = 0
num_max = 0

while True:
    
    numeros = int(input("Ingrese un numero positivo: "))
    
    if numeros > 0:
        numeros += suma_num
        numeros_procesados += 1
    elif numeros > num_max:
        num_max = numeros
    else:
        break
    
print(f"La suma total de todos los numeros ingresados es: {suma_num}")
print(f"El numero mas grande ingresado es {num_max}")
print(f"El numero total de numeros procesados es de {numeros_procesados}")
        
    

