palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou" # Una cadena con todas las vocales

for letra in palabra:
    if letra in vocales: # ¿Está la letra actual DENTRO de la cadena de vocales?
        print("*")
    else:
        print(letra)