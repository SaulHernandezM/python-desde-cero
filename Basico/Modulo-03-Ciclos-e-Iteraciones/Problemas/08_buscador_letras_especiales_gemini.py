# Corrección Problema 8: Buscador real
frase = "hola mundo"
encontrado = False
for letra in frase:
    if letra == "z":
        encontrado = True
        print("¡Letra crítica detectada!")
        break

if not encontrado:
    print("No se encontró la letra.")