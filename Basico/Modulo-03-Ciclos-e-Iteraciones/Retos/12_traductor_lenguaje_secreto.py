"""
Reto: El Traductor de "Lenguaje Secreto"
Este reto te enseñará a construir una respuesta letra por letra.
    Pide al usuario una palabra.
    Crea una variable vacía llamada palabra_secreta = "".
    Usa un bucle for para recorrer la palabra original.
    Lógica:
        Si la letra es una "p", añade una "b" a tu palabra_secreta.
        Si la letra es cualquier otra, añade la letra original.
        Pista: Para añadir letras usa palabra_secreta += letra.
    Al final: Imprime la palabra_secreta completa. (Ejemplo: "papa" se convierte en "baba").
"""

palabra = input("Ingresa una palabra: ")

palabra_secreta = " "

for letra in palabra:
    if letra == "p":
        palabra_secreta += "b"
    elif letra == "P":
        palabra_secreta += "B"
    else:
        palabra_secreta += letra

print(f"Palabra secreta: {palabra_secreta}")

"""
Tu lógica fue perfecta al manejar minúsculas y mayúsculas por separado. Solo un pequeño detalle técnico: 
inicializaste palabra_secreta = " " (con un espacio). En Python, eso significa que tu palabra final siempre 
empezará con un espacio vacío. Lo ideal es "" (cadena vacía).
"""

