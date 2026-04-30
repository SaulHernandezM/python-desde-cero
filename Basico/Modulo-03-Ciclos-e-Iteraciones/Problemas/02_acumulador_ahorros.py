"""
Problema: El Acumulador de Ahorros (for)
Objetivo: Practicar el uso de un acumulador dentro de un rango fijo.
    Descripción: Imagina que ahorras $5 cada día durante 30 días.
    Instrucciones: Crea un bucle for que vaya del día 1 al 30. En cada iteración, suma 5 a una variable llamada total_ahorro.
    Resultado esperado: Al final, el programa debe decir: "Tras 30 días, has ahorrado: $150".
"""

total_ahorro = 0
dia = 1

for x in range(1, 31):
    dinero_ingresado = float(input(f"Ingrese la cantidad a ingresar para el dia {dia}: "))
    
    total_ahorro += dinero_ingresado
    dia += 1
    

print(f"Tras 30 dias has ahorrado {total_ahorro} pesos")



