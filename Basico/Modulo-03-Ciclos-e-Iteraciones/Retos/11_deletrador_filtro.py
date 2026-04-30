"""
Reto: El "Deletreador" con Filtro
Este reto te ayudará a entender cómo manipular cada carácter.
    Pide al usuario una palabra (ej: "Python").
    Usa un for para recorrer la palabra.
    Lógica: - Debes imprimir cada letra de la palabra en una línea distinta.
    PERO, si la letra es una vocal (a, e, i, o, u), en lugar de la letra imprime un asterisco *.
    Ejemplo: 
            P
            y
            t
            h
            *
            n
"""

palabra = input("Ingrese una palabra: ").lower()
vocal = "a", "e", "i", "o", "u"

for letra in palabra:
    print(palabra)
    if palabra == vocal:
        vocal = "*"
        
    
    



