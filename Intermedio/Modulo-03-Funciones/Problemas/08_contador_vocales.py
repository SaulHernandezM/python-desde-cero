"""
Problema: El Contador de Vocales (Strings + Funciones)
Las funciones son perfectas para analizar texto.
    Crea una función llamada contar_vocales(texto).
    Misión: La función debe recorrer el texto y contar cuántas vocales (a, e, i, o, u) tiene.
    Retorno: Debe retornar el número total de vocales encontradas.
    Uso: Pide una frase al usuario y usa la función para decirle cuántas vocales tiene su frase.
"""

def contar_vocales(texto):
    contador = 0
    for vocal in texto:
        if vocal in "aeiou":
            contador += 1
    return contador


print("#### Contador de vocales ####")
frase = input("Frase: ").lower()

vocales_frase = contar_vocales(frase)

print(f"Vocales en la frase: {vocales_frase}.")

