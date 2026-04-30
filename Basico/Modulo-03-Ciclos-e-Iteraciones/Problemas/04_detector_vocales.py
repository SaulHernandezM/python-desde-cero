"""
Problema: El Detector de Vocales (for en cadenas)
Objetivo: Aprender que se puede iterar sobre texto, no solo números.
    Descripción: Queremos saber cuántas veces aparece la letra "a" (o "A") en una frase.
    Instrucciones: Pide al usuario que escriba una frase. Usa un for para recorrer cada letra de esa frase. 
    Si la letra es "a", suma 1 a un contador.
    Pista: for letra in frase: recorre el texto carácter por carácter.
    Resultado esperado: "La frase tiene X letras 'a'".
"""

frase = input("Escriba una frase: ").strip().lower()
contador = 0

for letra in frase:
    if letra == "a":
        contador += 1
   
   
print(f"La frase ―{frase} ―, tiene {contador} letras (a/A).")   
    






